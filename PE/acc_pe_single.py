import pylse

from helpers import *
from processing_element_8bit import processing_element

def s(x):
    return pylse.s(x, firing_delay=4.3)

def m(*args):
    return pylse.m(*args, firing_delay=8.2)

def dro(*args):
    return pylse.dro(*args, firing_delay=5.1)

    
def dro_c(*args):
    return pylse.dro_c(*args, firing_delay=5.1)

def pe(if_data, weight_data, wrt_ctrl, clk):
    """
    Processing Element

    Inputs:
        if_data: input feature data from the input feature memory
            Dimensions: 16 bits (dual-rail) -> 8 positive, 8 negative
        weight_data: weight data from the weight memory
            Dimensions: 16-bit (dual-rail signal), consisting of 8 positive + 8 negative bits
        wrt_ctrl: write control bit to reset the partial sum registers in the PEs
            Dimensions: 1 bit
        clk: clock signal
        NOTE: PE will operate at DR clock speeds
    
    Outputs:
        ofmap_out: output feature map
            Dimensions: 8 bits
    """

    # Split the clock
    clk_spl = pylse.split(clk, n=9, firing_delay=4.3)
    curr_clk_count = 0

    pe_out = processing_element(if_data, weight_data, wrt_ctrl, clk_spl[0])
    curr_clk_count += 1
    # pe_out is 8 bits

    # Use DRO_Cs to get the correct bits of the processing element output
    # Take the negative bit since the first 7 are flipped
    pe_out_arr = [dro_c(pe_out[i], clk_spl[curr_clk_count + i])[1] for i in range(7)]

    # Take the positive bit of the last output bit
    pe_out_7_p, _ = dro_c(pe_out[7], clk_spl[curr_clk_count + 7])
    pe_out_arr.append(pe_out_7_p)

    curr_clk_count += 8
    
    print("@@@ PE Clock Split Count:", curr_clk_count)

    return pe_out

def check_events(events, T, num_cycles):
    print("Output:")

    print("Cycle Num | ofmap_out")

    for i in range(num_cycles):
        print("Cycle " + str(i) + ":", end="")

        # Print out the corresponding if_mem_in bits going into that memory cell
        bits = []
        for j in range(8):
            bit = pulse_event_in_cycle(events, f'ofmap_out_bit{j}', T, i)
            bits.append(bit)
            print(bit, end="")

        int_val = twos_to_dec(bits)
        print("=" + str(int_val))
        
    
def gen_ifmap_inp(input_features):
    # Generate the dual-rail input feature signals
    # Input: input_features - array of integers
    #      Dimensions: 1 x num_cycles numbers
    print("Generating input feature signals:")

    if_bin = []
    # For each clock cycle
    for i in range(len(input_features)):
        # For each bit in the number
        bin_sig = twos_complement_bin(input_features[i])
        if_bin.append(bin_sig)
    
    if_bin_p = []
    if_bin_n = []
    # For each bit in the weight number
    for i in range(8):
        print("Bit " + str(i) + ":", end="")
        pulses_p = []
        pulses_n = []
        # For each clock cycle
        for j in range(len(if_bin)):
            print(if_bin[j][i], end="")
            if if_bin[j][i] == 1:
                pulses_p.append(j*T*2 + inp_delay)
                pulses_n.append(j*T*2 + T + inp_delay)
            else:
                pulses_p.append(j*T*2 + T + inp_delay)
                pulses_n.append(j*T*2 + inp_delay)

            
        print("")

        # Create the input signal
        inp_sig_p = pylse.inp_at(*pulses_p, name=f"if_bin_bit{i}_p")
        inp_sig_n = pylse.inp_at(*pulses_n, name=f"if_bin_bit{i}_n")
        if_bin_p.append(inp_sig_p)
        if_bin_n.append(inp_sig_n)

    ifmap_inp = if_bin_p + if_bin_n
    
    return ifmap_inp
    
def gen_weight_wrt_ctrl(weight_ints, wrt_ctrl):
    # Generate the PyLSE input signals given arrays of input features and write control signal at each clock cycle
    #   weight_ints: 1D array of 8-bit integers
    #       Dimensions: num_cycles x 1 number
    #   wrt_ctrl: 1D array of 1-bit, each element is the write control bit for a particular cycle
    #       Dimensions: num_cycles x 1 bit
    # Output:
    #   weights: 16 bits
    
    # Convert the input ints into binary signals
    weights_bin = []
    for i in range(len(weight_ints)):
        # For each clock cycle
        # Add the binary representation
        weights_bin.append(twos_complement_bin(weight_ints[i]))

    print(weight_ints)
    print(weights_bin)
    # weights_bin = transpose(weights_bin)
    print(len(weights_bin))
    print(len(weights_bin[0]))

    print("Weights In: ")
    # For each bit in the weight number
    weights = []
    for i in range(8):
        print("Bit " + str(i) + ": ")

        # For each cycle
        pulses_p = []
        pulses_n = []
        for k in range(len(weights_bin)):
            print(weights_bin[k][i], end="")
            if weights_bin[k][i] == 1:
                pulses_p.append(k*T*2 + inp_delay)
                pulses_n.append(k*T*2 + T + inp_delay)
            else:
                pulses_p.append(k*T*2 + T + inp_delay)
                pulses_n.append(k*T*2 + inp_delay)
            
        print("")

        # Create the input signal
        inp_sig_p = pylse.inp_at(*pulses_p, name=f"weights_bit{i}_p")
        inp_sig_n = pylse.inp_at(*pulses_n, name=f"weights_bit{i}_n")
            
        weights.append(inp_sig_p)
        weights.append(inp_sig_n)
    
    # Generate the input signals for write control bit
    wrt_ctrl_T = []
    for i in range(len(wrt_ctrl)):
        if wrt_ctrl[i] == 1:
            wrt_ctrl_T.append(i*T)
            
    wrt_ctrl = pylse.inp_at(*wrt_ctrl_T, name="wrt_ctrl")

    # Print out the dimensions of the input signals
    print("Dimensions of input weight signals:")
    print("weights: " + str(len(weights)) )
    
    return weights, wrt_ctrl


        
if __name__ == "__main__":
    T = 600
    num_cycles = 20
    clk = pylse.inp(start=T, period=T, n=num_cycles, name='clk')
    # clk_pe = pylse.inp(start=T/2, period=T/2, n=num_cycles, name='clk_pe')

    inp_delay = 50

    # Put some input feature numbers in
    input_features_ints = [8, 5, 8, 0, 8, 7, -2, 7, 9, 7, 9, -2, 6, 2, -1, -2, -5, 0, 8, 0, -1, -2, 4, 2,
                     1, -1, 6, -4, 2, -5, 23, 12]

    wrt_ctrl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Instantiate some weights
    weight_data_ints = [1, 2, 3, 1, 2, 5, -1, -20, 4, 5, 1, 0, 0, 1, -4, -1, -4, 1, 5, 6, 7, 8]

    weight_data, wrt_ctrl = gen_weight_wrt_ctrl(weight_data_ints, wrt_ctrl)

    input_features = gen_ifmap_inp(input_features_ints)

    ofmap_out = pe(input_features, weight_data, wrt_ctrl, clk)
    
    # Inspect the ofmap_out bits
    for i in range(8):
        pylse.inspect(ofmap_out[i], f"ofmap_out_bit{i}")
    
    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Check outputs
    check_events(events, T, num_cycles)