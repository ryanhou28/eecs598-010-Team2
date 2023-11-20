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

def processing_element(input_feature, weight_in, psum_in, clk):
    """
    An 8bit feature processing element.

    This design uses a shift-register memory with feedback to hold the weights.
    We may want to consider using an external DLM to storm these weights.

    parameters:
        input_feature
            8 wire pairs (positive, negative) for the input feature
        weight_in
            8 wire pairs (positive, negative) for the input weights
        psum_in
            8 wire pairs (positive, negative) for the input partial sum
        clk
            the clk signal
    
    """

    # Define some xSFQ cells we use in this module
    def dro(*args):
        return pylse.dro(*args, firing_delay=5.1)

    def dro_c(*args):
        return pylse.dro_c(*args, firing_delay=5.1)

    # How many cycles is the PE?
    N_BITS = 8

    # Split the clock signal
    clks = pylse.split(clk, n=32, firing_delay=4.3)
    current_clk_count = 0

    ##########################################################################
    # The Multiplier
    ##########################################################################

    mult_products = mult(input_feature[0], input_feature[1], input_feature[2], input_feature[3], input_feature[4], input_feature[5], input_feature[6], input_feature[7], input_feature[8], input_feature[9], input_feature[10], input_feature[11], input_feature[12], input_feature[13], input_feature[14], input_feature[15], weight_in[0], weight_in[1], weight_in[2], weight_in[3], weight_in[4], weight_in[5], weight_in[6], weight_in[7], weight_in[8], weight_in[9], weight_in[10], weight_in[11], weight_in[12], weight_in[13], weight_in[14], weight_in[15])

    mult_out = [dro_c(mult_products[i], clks[i]) for i in range(N_BITS)]
    current_clk_count += N_BITS

    # Pipeline the psum inputs with dros

    psum_dros = [dro(psum_in[i], clks[current_clk_count + i]) for i in range(N_BITS*2)]
    current_clk_count += N_BITS*2

    ##########################################################################
    # The Accumulator
    ##########################################################################

    # Note that mult's output at mult_out[7] is flipped, so the input is mult_out[7][1] = positive, mult_out[7][0] = negative
    adder_sum = adder(mult_out[0][0], mult_out[0][1], mult_out[1][0], mult_out[1][1], mult_out[2][0], mult_out[2][1], mult_out[3][0], mult_out[3][1], mult_out[4][0], mult_out[4][1], mult_out[5][0], mult_out[5][1], mult_out[6][0], mult_out[6][1], mult_out[7][1], mult_out[7][0], psum_dros[0], psum_dros[1], psum_dros[2], psum_dros[3], psum_dros[4], psum_dros[5], psum_dros[6], psum_dros[7], psum_dros[8], psum_dros[9], psum_dros[10], psum_dros[11], psum_dros[12], psum_dros[13], psum_dros[14], psum_dros[15])
    
    adder_out = [dro_c(adder_sum[i], clks[current_clk_count + i]) for i in range(N_BITS)]
    current_clk_count += N_BITS

    # Return the flipped bits, only the last output bit of the adder is correct
    pe_out = [adder_out[0][1], adder_out[1][1], adder_out[2][1], adder_out[3][1], adder_out[4][1], adder_out[5][1], adder_out[6][1], adder_out[7][0]]

    # Return the outputs pe_out, and some other wires for debugging
    return pe_out, mult_out, adder_out, mult_products

def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def test_single_input(input_feature_bin, weight_bin, psum_bin):
    # Test a single input
    input_feature_T = [[inv(int(input_feature_bin[i])), int(input_feature_bin[i])] for i in range(len(input_feature_bin))]
    weight_T = [[inv(int(weight_bin[i])), int(weight_bin[i])] for i in range(len(weight_bin))]
    psum_T = [[inv(int(psum_bin[i])), int(psum_bin[i])] for i in range(len(psum_bin))]
    input_features = []
    weights = []
    psums = []
    starting_delay = 100
    for i in range(8):
        input_features.append(pylse.inp_at(input_feature_T[i][0]*T + starting_delay, name=f"input_feature_{i}_p"))
        input_features.append(pylse.inp_at(input_feature_T[i][1]*T + starting_delay, name=f"input_feature_{i}_n"))
        weights.append(pylse.inp_at(weight_T[i][0]*T + starting_delay, name=f"weight_{i}_p"))
        weights.append(pylse.inp_at(weight_T[i][1]*T + starting_delay, name=f"weight_{i}_n"))
        psums.append(pylse.inp_at(psum_T[i][0]*T + starting_delay, name=f"psum_{i}_p"))
        psums.append(pylse.inp_at(psum_T[i][1]*T + starting_delay, name=f"psum_{i}_n"))

    return input_features, weights, psums


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
    T = 2000 # duration of a phase
    num_cycles = 5
    clk = pylse.inp(start=T/2, period=T, n=num_cycles, name='clk')

    input_feature_num = -28
    weight_num = 4
    psum_in = 127

    # Convert the numbers to binary
    input_feature_bin = twos_complement_bin(input_feature_num)
    weight_bin = twos_complement_bin(weight_num)
    psum_bin = twos_complement_bin(psum_in)

    print("Input Feature =", input_feature_num, "=", input_feature_bin)
    print("Weight =", weight_num, "=", weight_bin)
    print("Partial Sum =", psum_in, "=", psum_bin)

    input_features, weights, psums = test_single_input(input_feature_bin, weight_bin, psum_bin)

    # Instantiate the Processing Element
    PE_out, mult_out, adder_out, mult_products = processing_element(input_features, weights, psums, clk)

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