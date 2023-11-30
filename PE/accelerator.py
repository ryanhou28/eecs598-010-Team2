import pylse

from processing_element_8bit import processing_element
from feedback_mem_w_external_write import sr_N_bit_external_write, mux_s
from initialized_shift_register import create_sr_from_init_states, create_sr_from_int_list
from converters import alt_clock, sr_to_dr, dr_to_sr

def accelerator(input_features, clk, clk_o, clk_e):
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
    N_clocks = 578 # TODO: Update this with the actual number of clock splits needed
    N_clocks_o = 264
    N_clocks_e = 264
    N_num_cycles = 4 * 4 * 32 # TODO: Update this with the actual number of total clock cycles needed
    N_wrt_ctrl = 33

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
    curr_clk_o_count = 0
    curr_clk_e_count = 0
    # Split the clock signal
    clk_spl = pylse.split(clk, n=N_clocks, firing_delay=4.3)
    clk_o_spl = pylse.split(clk_o, n=N_clocks_o, firing_delay=4.3)
    clk_e_spl = pylse.split(clk_e, n=N_clocks_e, firing_delay=4.3)

    ##########################################################################
    # Write Control Memory
    ##########################################################################
    write_control_bits = [[1], [1], [0], [0], [0], [0]] # TODO: This is just a placeholder for now, add actual control signal!

    control_mem = create_sr_from_init_states([pylse.Wire()], clk_spl[curr_clk_count], write_control_bits)
    curr_clk_count += 1

    # control_mem is (N_num_cycles) deep, 1 bit wide
    curr_wrt_ctrl_count = 0

    # Split the reset signal
    # fanout for the ifmap and the psum buffers in the PEs
    wrt_ctrl_spl = pylse.split(control_mem[0], n=N_wrt_ctrl, firing_delay=4.3)

    ##########################################################################
    # Input Feature Memory
    ##########################################################################

    # Input Feature Memory will consist of 1 array of 8-bit wide 32 stages deep shift registers

    # Instantiate wires for input to the ifmap memory
    ofmap_in = [[pylse.Wire() for i in range(8)] for j in range(N_PE)]

    # Merge the input feature and the input from psums 
    # The merger essentially acts as a mux to select between input features and ofmap
    # This assumes the psums are initialized to 0s and that the input feature comes in at the first cycle
    if_mem_in = [[m(input_features[i][j], ofmap_in[i][j]) for i in range(N_PE)] for j in range(8)]

    if_data_sr = sr_N_bit_external_write(if_mem_in, wrt_ctrl_spl[curr_wrt_ctrl_count], clk_spl[curr_clk_count], N_PE, 8)

    curr_clk_count += 1
    curr_wrt_ctrl_count += 1

    # Convert the single rail output to dual rail
    p_list = []
    n_list = []
    for i in range(8):
        if_p, if_n = sr_to_dr(if_data_sr[i], clk_o_spl[i], clk_e_spl[i])
        p_list.append(if_p)
        n_list.append(if_n)
    if_data = p_list + n_list
    
    curr_clk_o_count += 8
    curr_clk_e_count += 8

    # Split the if_data 32 ways to each PE
    if_data_spl = [pylse.split(if_data[i], n=N_PE, firing_delay=4.3) for i in range(16)]

    # Transpose the split if_data for easier indexing
    if_data_spl = [list(row) for row in zip(*if_data_spl)]
    
    ##########################################################################
    # Weight Memory
    ##########################################################################

    # TODO: This is just a placeholder for now, add actual control signal!
    # Note that this is a single rail memory 8bits * N-num_cycles * N_PE
    weight_init_states = [[[0 for i in range(8)] for j in range(N_num_cycles)] for k in range(N_PE)] 

    # Weight memory is an array of 4 * 32 * 2 16-bit wide shift registers
    #   16-bit due to 8-bit positive and 8-bit negative pulses for each weight
    # We can change this so the bulk of the memory is only 8 bit wide with a final layer of dro_c to get the compliments

    # Create wires for feedback input to the weight memory
    weight_mem_in = [[pylse.Wire() for i in range(8)] for k in range(N_PE)]

    # Note that sr_weight_data_layers is single rail and needs to be converted to dual rail
    sr_weight_data_layers = [create_sr_from_init_states(weight_mem_in[i], clk_spl[curr_clk_count + i], weight_init_states[i]) for i in range(N_PE)]

    sr_weight_data = [[pylse.Wire() for i in range(8)] for j in range(N_PE)]

    # Split the output of the weight_memory
    for i in range(N_PE):
        for j in range(8):
            sr_weight_data[i][j], weight_mem_in[i][j] = s(sr_weight_data_layers[i][j])

    # Converts the single rail to dual rail
    # Dimensions are 32 x 8 x 2
    dr_weight_data_layers = []
    for weight in sr_weight_data:
        p_list = []
        n_list = []
        for w in weight:
            p, n = sr_to_dr(w, clk_o_spl[curr_clk_o_count], clk_e_spl[curr_clk_e_count])
            p_list.append(p)
            n_list.append(n)
            curr_clk_o_count += 1
            curr_clk_e_count += 1
        dr_weight_data_layers.append(p_list + n_list)
    
    curr_clk_count += N_PE

    ##########################################################################
    # Array of Processing Elements
    ##########################################################################

    pe_out = [processing_element(if_data_spl[i], dr_weight_data_layers[i], wrt_ctrl_spl[curr_wrt_ctrl_count + i], clk_spl[curr_clk_count + i]) for i in range(N_PE)]

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
    print("NUM CLOCK O SPLITS:", curr_clk_o_count)
    print("NUM CLOCK E SPLITS:", curr_clk_e_count)

    return nn_out, control_mem[0], pe_out

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

# Check Events
def check_events(events, T, num_cycles):
    print("Output Events")

    # For each cycle, ith cycle
    for i in range(num_cycles):

        print("CYCLE " + str(i) + ":")
        # For each PE, jth PE
        for j in range(32):
            outputs = [0 for i in range(8)]

            # For each bit of output, kth bit
            for k in range(8):

                pulse_this_cycle = False

                # For each event in this bit, mth event
                for m in range(len(events[f"PE{j}_out_{k}"])):
                    if events[f"PE{j}_out_{k}"][m] < i*T and events[f"PE{j}_out_{k}"][m] > (i-1)*T:
                        pulse_this_cycle = True
                outputs[k] = int(pulse_this_cycle)
            
            outstr = "PE[" + str(j) + "]:" + str(outputs)

            # Convert to decimal
            outdec = twos_to_dec(outputs)
            outstr += " = " + str(outdec)
            print(outstr)
        
        print("--------------------")

if __name__ == "__main__":
    # Define clock period
    T = 500
    num_cycles = 5
    clk = pylse.inp(start=T/2, period=T, n=num_cycles, name='clk')
    clk_e = pylse.inp(start=T/2, period=T*2, n=num_cycles, name='clk_e')
    clk_o = pylse.inp(start=T*2, period=T*2, n=num_cycles, name='clk_o')
    
    input_features = [0 for i in range(32)]
    
    input_feature_bin = [twos_complement_bin(input_features[i]) for i in range(len(input_features))]

    # Print out the input features
    print("Input Features:")
    print(input_features)

    # Generate the inputs
    input_features_pulses = test_single_input(input_feature_bin)

    nn_out, wrt_ctrl_out, pe_out  = accelerator(input_features_pulses, clk, clk_o, clk_e)

    # Probe outputs
    pylse.inspect(clk, 'clk')
    # TODO: Add probes for each output

    # Inspect the first PE output
    for i in range(8):
        pylse.inspect(nn_out[0][i], name=f"PE0_out_{i}")
        pylse.inspect(pe_out[0][i], name=f"PE0ReLU_out_{i}")
        
    pylse.inspect(wrt_ctrl_out, name=f"wrt_ctrl_out")

    # Run Simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
    # sim.print_state()

    # Check outputs
    check_events(events, T, num_cycles)