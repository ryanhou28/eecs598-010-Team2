"""
processing_element_8bit.py

The 8bit processing element is the building block of the systolic array
"""

import pylse
import shift_register, simple_memory, feedback_mem_w_external_write
import sys

sys.path.append('../')
from MAC.Adder.adder_8bit_syn_structural_N_PyLSE import adder, twos_to_dec, twos_complement_bin
from MAC.Mult.mult_comb_syn_structural_N_PyLSE import mult
from relu_syn_structural_N_PyLSE import relu
from initialized_shift_register import dro_sr_init_1, dro_init_1, dro_c_init_1
from converters import sr_to_dr, alt_clock

def processing_element(input_feature, weight_in, reset, clk):
    """
    An 8bit feature processing element.

    This design uses a shift-register memory with feedback to hold the weights outside the PE.
    Each PE holds a psum register (with reset).

    parameters (inputs):
        input_feature
            16 wires for the input feature
            [inp_0_p, inp_0_n, ...]
        weight_in
            16 wires to the input weights
            similarly structured to input_feature with alternating wires for each bit
        reset
            1 wire to reset the psum register
        clk
            the clk signal
    outputs:
        output_feature
            8-bit int output feature (after activation)
    """

    def dro_pair(x, clk):
        """
            xSFQ storage element consisting of two DRO cells in series.
        """
        # Split the clock
        clk_split = pylse.split(clk, 2)
        return pylse.dro(pylse.jtl(pylse.dro(pylse.jtl(x), clk_split[0])), clk_split[1])

    def dro_sr(*args):
        return pylse.dro_sr(*args, firing_delay=5.1)
    
    def dro(*args):
        """
        Destructive readout
        """
        return pylse.dro(*args, firing_delay=5.1)

    def dro_sr_pair(x, rst, clk):
        # xSFQ storage element consisting back to back DRO_SRs
        # Split the clock
        clk_split = pylse.split(clk, 2)
        # Split the reset signal
        rst_split = pylse.split(rst, 2)
        # Use dro_sr with initialized value of 1 since we want to start the psum register with a dual-railed zero value
        return dro_sr(pylse.jtl(dro_sr(pylse.jtl(x), rst_split[0], clk_split[0])), rst_split[1], clk_split[1])

    def dro_sr_sr1(x, rst, clk):
        # xSFQ storage element consisting of a DRO_SR connected to a DRO_SR initialized to 1
        # Split the clock
        clk_split = pylse.split(clk, 2)
        # Split the reset signal
        rst_split = pylse.split(rst, 2)
        # Use dro_sr with initialized value of 1 since we want to start the psum register with a dual-railed zero value
        return dro_sr(pylse.jtl(dro_sr_init_1(pylse.jtl(x), rst_split[0], clk_split[0])), rst_split[1], clk_split[1])
    
    def dro_sr1_sr(x, rst, clk):
        # xSFQ storage element consisting of a DRO_SR initialized to 1 connected to a DRO_SR
        # Split the clock
        clk_split = pylse.split(clk, 2)
        # Split the reset signal
        rst_split = pylse.split(rst, 2)
        # Use dro_sr with initialized value of 1 since we want to start the psum register with a dual-railed zero value
        return dro_sr_init_1(pylse.jtl(dro_sr(pylse.jtl(x), rst_split[0], clk_split[0])), rst_split[1], clk_split[1])

    def dro_sr_triple(x, rst, clk):
        clk_spl = pylse.split(clk, 3)
        rst_spl = pylse.split(rst, 3)
        return dro_sr(pylse.jtl(dro_sr(pylse.jtl(dro_sr(pylse.jtl(x), rst_spl[0], clk_spl[0])), rst_spl[1], clk_spl[1])), rst_spl[2], clk_spl[2])


    def dro_c(*args):
        return pylse.dro_c(*args, firing_delay=5.1)

    def s(x):
        return pylse.s(x, firing_delay=4.3)
    
    def dro1_dro_c(x, clk):
        clk0, clk1 = s(clk)
        return dro_c(dro_init_1(x, clk0), clk1)

    def dro1sr_dro_c(x, rst, clk):
        clk0, clk1 = s(clk)
        return dro_c(dro_sr_init_1(x, rst, clk0), clk1)
    
    def dro_sr_dro1_c(x, rst, clk):
        clk0, clk1 = s(clk)
        return dro_c_init_1(dro_sr(x, rst, clk0), clk1)

    def dro_dro1_c(x, clk):
        clk0, clk1 = s(clk)
        return dro_c_init_1(dro(x, clk0), clk1)

    # How many cycles is the PE?
    N_CYCLES = 2
    N_BITS = 8 # len(input_feature)

    # split clk
    clks = pylse.split(clk, n=100, firing_delay=4.3) # Need to adjust n=32 to the actual number of splitters needed
    current_clk_count = 0

    # clk_o, clk_e = alt_clk(clks[current_clk_count])
    # current_clk_count += 1

    # clks_o = pylse.split(clk_o, n=32, firing_delay=4.3)
    # clks_e = pylse.split(clk_e, n=32, firing_delay=4.3)
    # current_clk_o_count = 0
    # current_clk_e_count = 0

    # split reset
    resets = pylse.split(reset, n=32, firing_delay=4.3)
    current_rst_count = 0

    ##########################################################################
    # Multiplier
    ##########################################################################

    # Note that mult's output at mult_products[7] is flipped!
    mult_products = mult(input_feature[0], input_feature[1], input_feature[2], input_feature[3], input_feature[4], input_feature[5], input_feature[6], input_feature[7], input_feature[8], input_feature[9], input_feature[10], input_feature[11], input_feature[12], input_feature[13], input_feature[14], input_feature[15], weight_in[0], weight_in[1], weight_in[2], weight_in[3], weight_in[4], weight_in[5], weight_in[6], weight_in[7], weight_in[8], weight_in[9], weight_in[10], weight_in[11], weight_in[12], weight_in[13], weight_in[14], weight_in[15])

    mult_out = [dro1_dro_c(mult_products[i], clks[current_clk_count + i]) for i in range(7)]
    mult_out.append(dro_dro1_c(mult_products[7], clks[current_clk_count + 7]))
    current_clk_count += N_BITS * 2

    # Inspect mult output
    for i in range(8):
        pylse.inspect(mult_out[i][0], name=f"mult_out_{i}_p")
        pylse.inspect(mult_out[i][1], name=f"mult_out_{i}_n")

    ##########################################################################
    # Partial Sum Register
    ##########################################################################
    # First initializethe acc_out_split wires
    acc_out_p_split = [[pylse.Wire() for i in range(8)], [pylse.Wire() for i in range(8)]]
    acc_out_n_split = [[pylse.Wire() for i in range(8)], [pylse.Wire() for i in range(8)]]

    # The psum registers are 16 DRO_SR Pairs
    psum_dros = [pylse.Wire() for i in range(16)]
    for i in range(8):
        # Flip the inputs to the DROs
        # psum_dros[2*i] <<= dro_sr(acc_out_n_split[0][i], resets[current_rst_count], clks[current_clk_count])
        # psum_dros[2*i + 1] <<= dro_sr_init_1(acc_out_p_split[0][i], resets[current_rst_count + 1], clks[current_clk_count + 1])
        # psum_dros[2*i] <<= dro_sr_triple(acc_out_n_split[0][i], resets[current_rst_count], clks[current_clk_count])
        # psum_dros[2*i + 1] <<= dro_sr_triple(acc_out_p_split[0][i], resets[current_rst_count + 1], clks[current_clk_count + 1])
        psum_dros[2*i] <<= acc_out_p_split[0][i]
        psum_dros[2*i + 1] <<= acc_out_n_split[0][i]

        current_clk_count += 2
        current_rst_count += 2

    # Inspect psum
    for i in range(8):
        pylse.inspect(psum_dros[2*i], name=f"psum_{i}_p")
        pylse.inspect(psum_dros[2*i + 1], name=f"psum_{i}_n")

    ##########################################################################
    # Accumulator
    ##########################################################################
    adder_sum = adder(mult_out[0][0], mult_out[0][1], mult_out[1][0], mult_out[1][1], mult_out[2][0], mult_out[2][1], mult_out[3][0], mult_out[3][1], mult_out[4][0], mult_out[4][1], mult_out[5][0], mult_out[5][1], mult_out[6][0], mult_out[6][1], mult_out[7][1], mult_out[7][0], psum_dros[0], psum_dros[1], psum_dros[2], psum_dros[3], psum_dros[4], psum_dros[5], psum_dros[6], psum_dros[7], psum_dros[8], psum_dros[9], psum_dros[10], psum_dros[11], psum_dros[12], psum_dros[13], psum_dros[14], psum_dros[15])
    
    # Inspect adder output
    for i in range(8):
        pylse.inspect(adder_sum[i], name=f"adder_sum_{i}")

    # Pipeline adder output
    adder_out = []
    for i in range(8):
        if i == 7:
            # ONLY THE MSB OF THE ADDER OUTPUT IS FLIPPED
            adder_out.append(dro_sr_dro1_c(adder_sum[i], resets[current_rst_count], clks[current_clk_count]))
        else:
            adder_out.append(dro1sr_dro_c(adder_sum[i], resets[current_rst_count], clks[current_clk_count]))
        
        current_rst_count += 1
        current_clk_count += 1
    # adder_out = [dro1sr_dro_c(adder_sum[i], resets[current_rst_count + i], clks[current_clk_count + i]) for i in range(N_BITS)]

    current_clk_count += N_BITS
    current_rst_count += N_BITS

    # Return the correctly flipped bits, only the last output bit of the adder needs to be flipped
    acc_out_p = [adder_out[0][0], adder_out[1][0], adder_out[2][0], adder_out[3][0], adder_out[4][0], adder_out[5][0], adder_out[6][0], adder_out[7][1]]
    acc_out_n = [adder_out[0][1], adder_out[1][1], adder_out[2][1], adder_out[3][1], adder_out[4][1], adder_out[5][1], adder_out[6][1], adder_out[7][0]]

    # split the accumulator_out into 2 for:
    # 0 -> the accumulator memory
    # 1 -> the ReLU unit
    for i in range(N_BITS):
        acc_p0, acc_p1 = s(acc_out_p[i])
        acc_out_p_split[0][i] <<= acc_p0
        acc_out_p_split[1][i] <<= acc_p1

        acc_n0, acc_n1 = s(acc_out_n[i])
        acc_out_n_split[0][i] <<= acc_n0
        acc_out_n_split[1][i] <<= acc_n1

    ##########################################################################
    # ReLU
    ##########################################################################

    # Note: output of ReLU has all bits flipped except for the MSB
    pe_out = relu(acc_out_p_split[1][0], acc_out_n_split[1][0], acc_out_p_split[1][1], acc_out_n_split[1][1], acc_out_p_split[1][2], acc_out_n_split[1][2], acc_out_p_split[1][3], acc_out_n_split[1][3], acc_out_p_split[1][4], acc_out_n_split[1][4], acc_out_p_split[1][5], acc_out_n_split[1][5], acc_out_p_split[1][6], acc_out_n_split[1][6], acc_out_p_split[1][7], acc_out_n_split[1][7])

    return pe_out

def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def test_input(input_features, weights, resets):
    inp_delay = 100 + T

    # Convert input numbers to binary signals
    if_bin = []
    for i in range(len(input_features)):
        bin_sig = twos_complement_bin(input_features[i])
        if_bin.append(bin_sig)
    
    weights_bin = []
    for i in range(len(weights)):
        # For each clock cycle
        # Add the binary representation
        weights_bin.append(twos_complement_bin(weights[i]))

    ifmap_in = []
    weights_sig = []
    # For each bit in the input numbers
    for i in range(8):
        print("Bit " + str(i) + ":", end="")
        pulses_p = []
        pulses_n = []
        weight_pulses_p = []
        weight_pulses_n = []
        # For each clock cycle
        for j in range(len(if_bin)):
            print(if_bin[j][i], end="")
            if if_bin[j][i] == 1:
                pulses_p.append(j*T*2 + inp_delay)
                pulses_n.append(j*T*2 + T + inp_delay)
            else:
                pulses_p.append(j*T*2 + T + inp_delay)
                pulses_n.append(j*T*2 + inp_delay)
            
            # Add the weight bin numbers
            if weights_bin[j][i] == 1:
                weight_pulses_p.append(j*T*2 + inp_delay)
                weight_pulses_n.append(j*T*2 + T + inp_delay)
            else:
                weight_pulses_p.append(j*T*2 + T + inp_delay)
                weight_pulses_n.append(j*T*2 + inp_delay)
        
        print("")

        # Create the input signal
        inp_sig_p = pylse.inp_at(*pulses_p, name=f"input_feature_bit{i}_p")
        inp_sig_n = pylse.inp_at(*pulses_n, name=f"input_feature_bit{i}_n")
        ifmap_in.append(inp_sig_p)
        ifmap_in.append(inp_sig_n)

        weight_inp_sig_p = pylse.inp_at(*weight_pulses_p, name=f"weight_bit{i}_p")
        weight_inp_sig_n = pylse.inp_at(*weight_pulses_n, name=f"weight_bit{i}_n")

        weights_sig.append(weight_inp_sig_p)
        weights_sig.append(weight_inp_sig_n)
    
    # Generate reset signals
    reset_pulses = []
    for i in range(len(resets)):
        if resets[i] == 1:
            reset_pulses.append(i*T + inp_delay)
    
    reset_pulses = pylse.inp_at(*reset_pulses, name="reset")

    return ifmap_in, weights_sig, reset_pulses

def test_single_input(input_feature_bin, weight_bin, reset_bin):
    # Test a single input
    input_feature_T = [[inv(int(input_feature_bin[i])), int(input_feature_bin[i])] for i in range(len(input_feature_bin))]
    weight_T = [[inv(int(weight_bin[i])), int(weight_bin[i])] for i in range(len(weight_bin))]
    reset_T = inv(int(reset_bin))
    input_features = []
    weights = []
    starting_delay = 50
    for i in range(8):
        input_features.append(pylse.inp_at(input_feature_T[i][0] + starting_delay, name=f"input_feature_{i}_p"))
        input_features.append(pylse.inp_at(input_feature_T[i][1] + starting_delay, name=f"input_feature_{i}_n"))
        weights.append(pylse.inp_at(weight_T[i][0]*T + starting_delay, name=f"weight_{i}_p"))
        weights.append(pylse.inp_at(weight_T[i][1]*T + starting_delay, name=f"weight_{i}_n"))

    reset = pylse.inp_at(reset_T*T + starting_delay, name=f"reset")

    return input_features, weights, reset


# Check Events
def check_events(events, T, num_cycles):
    print("Output Events")

    # For each cycle, ith cycle
    for i in range(num_cycles):
        outputs = [0, 0, 0, 0, 0, 0, 0, 0]

        for j in range(8):
            # For each bit of output, jth bit
            pulse_this_cycle = False
            for k in range(len(events[f"PE_out_{j}"])):
                # For each event in this bit, kth event
                if events[f"PE_out_{j}"][k] < i*T and events[f"PE_out_{j}"][k] > (i-1)*T:
                    pulse_this_cycle = True
            outputs[j] = int(pulse_this_cycle)
        
        outstr = "[" + str(i) + "]:" + str(outputs)

        # Convert to decimal
        outdec = twos_to_dec(outputs)
        outstr += " = " + str(outdec)
        print(outstr)

if __name__ == "__main__":
    # Create clock signal
    T = 1000 # duration of a phase
    num_cycles = 20
    clk = pylse.inp(start=T, period=T, n=num_cycles, name='clk')

    input_feature_num = 8
    weight_num = 4

    # Convert the numbers to binary
    input_feature_bin = twos_complement_bin(input_feature_num)
    weight_bin = twos_complement_bin(weight_num)
    reset_bin = 0

    # print("Input Feature =", input_feature_num, "=", input_feature_bin)
    # print("Weight =", weight_num, "=", weight_bin)

    # input_features, weights, reset = test_single_input(input_feature_bin, weight_bin, reset_bin)

    input_feature_nums = [9, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    weight_nums = [10, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    resets = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    input_features, weights, reset = test_input(input_feature_nums, weight_nums, resets)

    # Instantiate the Processing Element
    PE_out = processing_element(input_features, weights, reset, clk)

    # Probe outputs
    for i in range(8):
        pylse.inspect(PE_out[i], name=f"PE_out_{i}")
    
    # Debug outputs
    # for i in range(8):
        # if (i == 7):
            # Flip the correct bit
            # pylse.inspect(mult_out[i][0], name=f"mult_out_{i}_n")
            # pylse.inspect(mult_out[i][1], name=f"mult_out_{i}_p")
            # pylse.inspect(adder_out[i][0], name=f"adder_out_{i}_p")
            # pylse.inspect(adder_out[i][1], name=f"adder_out_{i}_n")
        # else:
            # pylse.inspect(mult_out[i][0], name=f"mult_out_{i}_p")
            # pylse.inspect(mult_out[i][1], name=f"mult_out_{i}_n")
            # pylse.inspect(adder_out[i][0], name=f"adder_out_{i}_n")
            # pylse.inspect(adder_out[i][1], name=f"adder_out_{i}_p")
        
        # pylse.inspect(mult_products[i], name=f"mult_products_{i}")
    
    # Run Simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Print out the events cycle by cycle
    check_events(events, T, num_cycles)