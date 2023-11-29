import pylse

from processing_element_8bit import processing_element
from feedback_mem_w_external_write import sr_N_bit_external_write, mux_s
from initialized_shift_register import create_sr_from_init_states, create_sr_from_int_list

def accelerator(input_features, clk):
    """ Accelerator
    
    Inputs:
        input_features: 32 x 16 bit array of input features
            16 bits for 8 positive and 8 negative pulses representing a 8-bit two's complement integer
        clk: clock signal
    Outputs:
        nn_out: 32 x 16 bit array of output features (TODO: or output only the 8 positive bits)

    """
    # Define constants
    N_PE = 32
    N_clocks = 1000 # TODO: Update this with the actual number of clock splits needed
    N_resets = 1000 # TODO: Update this with the actual number of reset splits needed
    N_num_cycles = 100 # TODO: Update this with the actual number of total clock cycles needed

    ##########################################################################
    # Define xSFQ cells needed
    ##########################################################################

    def m(*args):
        return pylse.m(*args, firing_delay=8.2)
    
    def s(x):
        return pylse.s(x, firing_delay=4.3)

    ##########################################################################
    # Clock
    ##########################################################################

    # Initialize counting variables
    curr_clk_count = 0
    # Split the clock signal
    clk_spl = pylse.split(clk, n=N_clocks, firing_delay=4.3)

    ##########################################################################
    # Write Control Memory
    ##########################################################################
    write_control_bits = [[0], [1], [0], [0], [0], [0]] # TODO: This is just a placeholder for now, add actual control signal!

    control_mem = create_sr_from_init_states([pylse.Wire()], clk_spl[curr_clk_count], write_control_bits)
    curr_clk_count += 1

    # control_mem is (N_num_cycles) deep, 1 bit wide
    curr_wrt_ctrl_count = 0

    # Split the reset signal
    # fanout for the ifmap and the psum buffers in the PEs
    wrt_ctrl_spl = pylse.split(control_mem[0], n=96, firing_delay=4.3)

    ##########################################################################
    # Input Feature Memory
    ##########################################################################

    # Input Feature Memory will consist of 2 arrays of 8-bit wide 16 stages deep shift registers
    #  One array will be the positive pulses for input feature memory, and the other containing the negative values
    #  Both arrays need to be 2 * 8 = 16 stages deep due to alternating phases of xSFQ 

    # Instantiate wires for input to the ifmap memory
    ofmap_in = [[pylse.Wire() for i in range(16)] for i in range(N_PE)]

    # Connect the input feature pulses to the corresponding shift register
    if_mem_in = []
    for i in range(N_PE):
        # Merge the input feature and the input from psums
        #   The merger essentially acts as a mux to select between input features and ofmap
        #   This assumes the psums are initialized to 0s and that the input feature comes in at the first cycle
        if_mem_in_layer = [m(input_features[i][j], ofmap_in[i][j]) for j in range(16)]

        if_mem_in.append(if_mem_in_layer)

        # Skip one layer of the DROs for correct alternating phase
        if_mem_in.append([pylse.Wire() for i in range(16)])

    if_data = sr_N_bit_external_write(if_mem_in, wrt_ctrl_spl[curr_wrt_ctrl_count], clk_spl[curr_clk_count], 16, N_PE*2)
    curr_clk_count += 1
    curr_wrt_ctrl_count += 1

    ##########################################################################
    # Weight Memory
    ##########################################################################

    weight_init_states = [[[0 for i in range(8)] + [1 for i in range(8)] for j in range(N_num_cycles)] for k in range(N_PE)] # TODO: This is just a placeholder for now, add actual control signal!

    # Weight memory is an array of 4 * 32 * 2 16-bit wide shift registers
    #   16-bit due to 8-bit positive and 8-bit negative pulses for each weight
    # We can change this so the bulk of the memory is only 8 bit wide with a final layer of dro_c to get the compliments

    # Create wires for feedback input to the weight memory
    weight_mem_in = [[pylse.Wire() for i in range(16)] for k in range(N_PE)]

    weight_data_layers = [create_sr_from_init_states(weight_mem_in[i], clk_spl[curr_clk_count + i], weight_init_states[i]) for i in range(N_PE)]

    weight_data = [[pylse.Wire() for i in range(16)] for i in range(N_PE)]

    # Split the output of the weight_memory
    for i in range(N_PE):
        for j in range(16):
            weight_data[i][j], weight_mem_in[i][j] = s(weight_data_layers[i][j])
    
    curr_clk_count += N_PE

    ##########################################################################
    # Array of Processing Elements
    ##########################################################################

    pe_out = [processing_element(if_data[i], weight_data[i], wrt_ctrl_spl[curr_wrt_ctrl_count + i], clk_spl[curr_clk_count + i]) for i in range(N_PE)]

    curr_clk_count += N_PE
    curr_wrt_ctrl_count += N_PE

    # NOTE: pe_out is structured as an array of 8 wires, where all but the last wire (MSB) are inverted values
    # so we need to invert the values to get the correct output when connecting to the memories
    # Use DRO_C s to invert the output and a dro to delay it
    # This will require two more clock cycles
    inverted_delayed_pe_out = []
    for i in range(N_PE):
        single_pe = pe_out[i]
        # The ouput from a single PE (8 bits)
        # We then need to flip all but the last wire
        inverted_delayed_single_pe = []
        for j in range(8):
            if j < 7: # Not the last bit, so we invert
                inverted_delayed_single_pe.append(pylse.dro(pylse.dro_c(single_pe[j], clk_spl[curr_clk_count])[1], clk_spl[curr_clk_count+1]))
            else: # The last bit so we don't invert
                inverted_delayed_single_pe.append(pylse.dro(pylse.dro(single_pe[j], clk_spl[curr_clk_count]), clk_spl[curr_clk_count+1]))
            curr_clk_count += 2
        inverted_delayed_pe_out.append(inverted_delayed_single_pe)

    split_inverted_delayed_pe_out = [[s(o) for o in s_pe] for s_pe in inverted_delayed_pe_out]

    # Connect the output of the PEs to the ifmap memory
    ofmap_in = [[o[0] for o in s_pe] for s_pe in split_inverted_delayed_pe_out]

    nn_out = [[o[1] for o in s_pe] for s_pe in split_inverted_delayed_pe_out]

    print("NUM CLOCK SPLITS:", curr_clk_count)
    print("NUM WRT CTRL SPLITS:", curr_wrt_ctrl_count)

    return nn_out

def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def twos_to_dec(binary_array):
    # Convert a binary array of bits of the 8-bit twos complement to a decimal number
    if not binary_array:
        return 0

    # Check if the number is negative (MSB is 1)
    is_negative = binary_array[-1] == 1

    if is_negative:
        # Invert the bits
        inverted_array = [1 - bit for bit in binary_array]

        # Add 1 to the inverted array
        carry = 1
        for i in range(len(inverted_array)):
            inverted_array[i] += carry
            if inverted_array[i] == 2:
                inverted_array[i] = 0
                carry = 1
            else:
                carry = 0

        # Convert to number and negate
        number = -sum(bit * (2 ** i) for i, bit in enumerate(inverted_array))
    else:
        # Convert to number directly
        number = sum(bit * (2 ** i) for i, bit in enumerate(binary_array))

    return number

def twos_complement_bin(num):
    # Generate a binary array of bits of the 8-bit twos complement of the number
    # Saturate the bit array if the number is out of range
    if num < -128:
        num = -128
    elif num > 127:
        num = 127

    if num < 0:
        num = 256 + num

    bin_str = bin(num)[2:].zfill(8)

    binarr = [int(x) for x in bin_str]

    # Flip the binarr so that the LSB is at the beginning
    binarr.reverse()

    return binarr

def test_single_input(input_feature_bin_arr):
    # Test a single input

    input_features_arr = []
    for input_feature_bin in input_feature_bin_arr:
        input_feature_T = [[inv(int(input_feature_bin[i])), int(input_feature_bin[i])] for i in range(len(input_feature_bin))]
        input_features = []
        starting_delay = 100
        for i in range(8):
            input_features.append(pylse.inp_at(input_feature_T[i][0]*T + starting_delay, name=f"input_feature_{i}_p"))
            input_features.append(pylse.inp_at(input_feature_T[i][1]*T + starting_delay, name=f"input_feature_{i}_n"))
        
        input_features_arr.append(input_features)

    return input_features_arr

if __name__ == "__main__":
    # Define clock period
    T = 500
    clk = pylse.inp(start=T/2, period=T, n=10, name='clk')
    
    input_features = [0 for i in range(32)]
    
    input_feature_bin = [twos_complement_bin(input_features[i]) for i in range(len(input_features))]

    # Print out the input features
    print("Input Features:")
    print(input_features)

    # Generate the inputs
    input_features_pulses = test_single_input(input_feature_bin)

    pe_out = accelerator(input_features_pulses, clk)

    # Probe outputs
    pylse.inspect(clk, 'clk')
    # TODO: Add probes for each output

    # Run Simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Check outputs
    # TODO