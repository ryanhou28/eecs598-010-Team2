import pylse

from helpers import *
from feedback_mem_w_external_write import sr_N_bit_external_write
from converters import alt_clock, sr_to_dr, dr_to_sr

def s(x):
    return pylse.s(x, firing_delay=4.3)

def m(*args):
    return pylse.m(*args, firing_delay=8.2)

def ifmap_mem(input_features, ofmap_in, wrt_ctrl, clk, clk_o, clk_e):
    """
    Input Feature Map Memory

    Inputs:
        input_features: input_featurs from the quantum readout circuit
            Dimensions: 8 bits x 32 ints
        ofmap_in: output feature map from the PEs
            Dimensions: 8 bits x 32 ints
        wrt_ctrl: write control bits from the write control memory
            Dimensions: 1 bit
        clk: clock signal
    
    Outputs:
        ifmap_out: one input feature integer for the next layer of computation
            Dimensions: an array of 16 bits (dual-rail) -> 8 positive, 8 negative
    """

    # Merge the input feature and ofmap
    #   Essentially acting as a mux to select between input features and ofmap
    #   Assumes the psums are initialized to 0s and that the input features comes in at the first cycle
    if_mem_in = [[m(input_features[i][j], ofmap_in[i][j]) for j in range(32)] for i in range(8)]

    # Inspect internal merger signal
    for i in range(8):
        for j in range(32):
            pylse.inspect(if_mem_in[i][j], f"if_mem_in_int{j}_bit{i}")

    if_data_sr = sr_N_bit_external_write(if_mem_in, wrt_ctrl, clk, 32, 8)
    # Split the alternating clock signals
    clk_o_spl = pylse.split(clk_o, n=8, firing_delay=4.3)
    clk_e_spl = pylse.split(clk_e, n=8, firing_delay=4.3)

    # Convert single-rail to dual-rail
    p_list = []
    n_list = []
    for i in range(8):
        if_p, if_n = sr_to_dr(if_data_sr[i], clk_o_spl[i], clk_e_spl[i])
        p_list.append(if_p)
        n_list.append(if_n)
    if_data = p_list + n_list

    return if_data

def check_events(events, T, num_cycles):
    print("Output:")

    print("Cycle Num | wrt_ctrl| Cycle E | Cycle O | if_out_p | if_out_n | if_mem_in (int 0 ... 31)")

    for i in range(num_cycles):
        print("Cycle " + str(i) + ":", end="")

        print(pulse_event_in_cycle(events, 'wrt_ctrl', T, i), end="|")
        print(pulse_event_in_cycle(events, 'clk_e', T, i), end="|")
        print(pulse_event_in_cycle(events, 'clk_o', T, i), end="|")

        bits = []
        # For each bit of the output (positive)
        for j in range(8):
            bit = pulse_event_in_cycle(events, f'if_out_{j}_p', T, i)
            print(bit, end="")
            bits.append(bit)
        
        # Convert to int
        int_val = twos_to_dec(bits)
        print("=" + str(int_val), end="|")

        # For each bit of the output (negative)
        for j in range(8):
            bit = pulse_event_in_cycle(events, f'if_out_{j}_n', T, i)
            print(bit, end="")
        
        print("|", end="")

        # For each integer
        for j in range(32):
            # Print out the corresponding if_mem_in bits going into that memory cell
            bits = []
            for k in range(8):
                bit = pulse_event_in_cycle(events, f'if_mem_in_int{j}_bit{k}', T, i)
                bits.append(bit)
                print(bit, end="")

            int_val = twos_to_dec(bits)
            print("=" + str(int_val), end="|")
        
        print("")
        

def gen_inp(input_features_ints, ofmap_in_ints, wrt_ctrl):
    # Generate the PyLSE input signals given arrays of inputs at each clock cycle
    #   input_features_ints: 2D array of 8-bit integers, each row is an array of ints for each clock cycle
    #   ofmap_in_ints: same dimensions as above
    #   wrt_ctrl: 1D array of 1-bit, each element is the write control bit for each clock cycle
    
    # Convert the input ints into binary signals
    input_feats_bin = []
    for i in range(len(input_features_ints)):
        # For each clock cycle
        pe_bin_arr = []
        for j in range(len(input_features_ints[i])):
            # For each integer in this cycle
            bin_sig = twos_complement_bin(input_features_ints[i][j])
            pe_bin_arr.append(bin_sig)
        input_feats_bin.append(pe_bin_arr)
    print(input_features_ints)
    print(input_feats_bin)
    # input_feats_bin = transpose(input_feats_bin)
    print(len(input_feats_bin))
    print(len(input_feats_bin[0]))
    print(len(input_feats_bin[0][0]))

    print("Input features: ")
    # For each bit in the input feature number
    input_features = []
    for i in range(8):
        print("Bit " + str(i) + ": ")
        pe_pulse_arr = []
        # For each input feature number for each PE
        for j in range(32):
            print("int " + str(j) + ": ")
            # For each cycle
            pulses = []
            for k in range(len(input_feats_bin)):
                print(input_feats_bin[k][j][i], end="")
                if input_feats_bin[k][j][i] == 1:
                    pulses.append(k*T)
                
            print("")

            # Create the input signal
            inp_sig = pylse.inp_at(*pulses, name=f"input_feature_int{j}_bit{i}")
            pe_pulse_arr.append(inp_sig)
        input_features.append(pe_pulse_arr)
    
    # Creat ofmap input signals
    print("--------------------")
    print("Output feature map: ")
    # First convert the numbers to twos complement binary
    ofmap_in_bin = []
    for i in range(len(ofmap_in_ints)):
        # For each clock cycle
        pe_bin_arr = []
        for j in range(len(ofmap_in_ints[i])):
            # For each integer in this cycle
            bin_sig = twos_complement_bin(ofmap_in_ints[i][j])
            pe_bin_arr.append(bin_sig)
        ofmap_in_bin.append(pe_bin_arr)
    
    # Generate the input signals for ofmap_in
    ofmap_in = []
    # For each bit in the output feature number
    for i in range(8):
        print("Bit " + str(i) + ": ")
        pe_pulse_arr = []
        # For each input feature number for each PE
        for j in range(32):
            print("int " + str(j) + ": ")
            # For each cycle
            pulses = []
            for k in range(len(ofmap_in_bin)):
                print(ofmap_in_bin[k][j][i], end="")
                if ofmap_in_bin[k][j][i] == 1:
                    pulses.append(k*T)
            print("")

            # Create the input signal
            inp_sig = pylse.inp_at(*pulses, name=f"ofmap_in_int{j}_bit{i}")
            pe_pulse_arr.append(inp_sig)
        ofmap_in.append(pe_pulse_arr)

    # Generate the input signals for write control bit
    wrt_ctrl_T = []
    for i in range(len(wrt_ctrl)):
        if wrt_ctrl[i] == 1:
            wrt_ctrl_T.append(i*T)
            
    wrt_ctrl = pylse.inp_at(*wrt_ctrl_T, name="wrt_ctrl")

    # Print out the dimensions of the input signals
    print("Dimensions of input signals:")
    print("input_features: " + str(len(input_features)) + " x " + str(len(input_features[0])))
    print("ofmap_in: " + str(len(ofmap_in)) + " x " + str(len(ofmap_in[0])))
    
    return input_features, ofmap_in, wrt_ctrl
        
if __name__ == "__main__":
    T = 50
    num_cycles = 12
    clk = pylse.inp(start=T, period=T, n=num_cycles, name='clk')
    # Split the clock
    clk0, clk1 = s(clk)
    clk_o, clk_e = alt_clock(clk0)

    # These are real input features from fnn_32.py
    input_feats_init = [-8, -5, 8, 0, 8, 7, -2, 7, 9, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0]
    # Flip the array
    input_feats_init = input_feats_init[::-1]

    zero_ins = [0 for i in range(32)]
    input_features_ints = [input_feats_init] + [zero_ins for i in range(num_cycles-1)]

    # These are some fake numbers to put in
    ofmap_in_nums = [9, 1, -9, -10, 9, 2, -1, 1, 3, 6, 10, 23, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 13, -123, 14, 23, -100, 10]
    # ofmap_in_ints = [zero_ins for i in range(5)] + [ofmap_in_nums for i in range(num_cycles-6)]
    ofmap_in_ints = [zero_ins for i in range(num_cycles)]

    wrt_ctrl = [1] + [0 for i in range(6)] + [0 for i in range(5)]
    
    input_features, ofmap_in, wrt_ctrl = gen_inp(input_features_ints, ofmap_in_ints, wrt_ctrl)

    if_out = ifmap_mem(input_features, ofmap_in, wrt_ctrl, clk1, clk_o, clk_e)

    # pylse.inspect(clk1, 'clk')
    pylse.inspect(clk_o, 'clk_o')
    pylse.inspect(clk_e, 'clk_e')
    
    # Inspect the if_out bits
    for i in range(8):
        pylse.inspect(if_out[i], f"if_out_{i}_p")
    
    for i in range(8, 16):
        pylse.inspect(if_out[i], f"if_out_{i-8}_n")

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Check outputs
    check_events(events, T, num_cycles)