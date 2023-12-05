import pylse
import sys
sys.path.append('../')
from helpers import *
from pylse_event_print import *
from PE.processing_element_8bit import processing_element
from MEM.feedback_mem_w_external_write import sr_N_bit_external_write, mux_s
from MEM.initialized_shift_register import create_sr_from_init_states, create_sr_from_int_list
from converters import alt_clock, sr_to_dr, dr_to_sr
from Accelerator.acc_ifmap_mem import ifmap_mem
from Accelerator.acc_weight_mem import weight_mem
from Accelerator.acc_pe_array import pe_array
from Accelerator.acc_wrt_ctrl import write_control_mem

def accelerator(input_features, write_control_bits, weights_init, clk, clk_dr, clk_o, clk_e, clk_wrt_ctrl):
    """ Accelerator
    
    Inputs:
        input_features: input_features from the quantum readout circuit
            Dimensions: 8 bits x 32 ints
        write_control_bits: array of write control bits
        weights_init: initial weights for the neural network
            Dimensions: 32 x N integer 2D array
        clk: clock signal
    Outputs:
        nn_out: 32 x 16 bit array of output features (TODO: or output only the 8 positive bits)

    """
    ##########################################################################
    # Define xSFQ cells needed
    ##########################################################################

    def m(*args):
        return pylse.m(*args, firing_delay=8.2)
    
    def s(x):
        return pylse.s(x, firing_delay=4.3)

    def dro(*args):
        return pylse.dro(*args, firing_delay=5.1)

    ##########################################################################
    # Clock
    ##########################################################################

    # Initialize counting variables
    curr_clk_count = 0
    # Split the clock signal
    clks = pylse.split(clk, n=2, firing_delay=4.3)
    clk_o_0, clk_o_1 = s(clk_o)
    clk_e_0, clk_e_1 = s(clk_e)

    ##########################################################################
    # Write Control Memory
    ##########################################################################
    wrt_ctrl_bit = write_control_mem(write_control_bits, clk_wrt_ctrl)
    # wrt_ctrl_bit is 1 bit

    # Inspect internal wire
    # pylse.inspect(wrt_ctrl_bit, name="acc_wrt_ctrl_bit")

    # Split the reset signal
    # fanout for the ifmap and the psum buffers in the PEs
    wrt_ctrl_0, wrt_ctrl_1 = s(wrt_ctrl_bit)

    ##########################################################################
    # Input Feature Memory
    ##########################################################################

    # Input Feature Memory will consist of 1 array of 8-bit wide 32 stages deep shift registers

    # Instantiate wires for input to the ifmap memory
    ofmap_in = [[pylse.Wire() for i in range(32)] for j in range(8)]

    if_data = ifmap_mem(input_features, ofmap_in, wrt_ctrl_0, clks[0], clk_o_0, clk_e_0)

    # Inspect the if_data
    for i in range(8):
        pylse.inspect(if_data[2*i], name=f"acc_if_data_bit_{i}_p")
        pylse.inspect(if_data[2*i + 1], name=f"acc_if_data_bit_{i}_n")
    
    for i in range(8):
        # Inspect one of the ofmap_in wires
        pylse.inspect(ofmap_in[i][0], name=f"acc_ofmap_in0_bit_{i}")
    
    ##########################################################################
    # Weight Memory
    ##########################################################################

    dr_weight_data = weight_mem(weights_init, clks[1], clk_o_1, clk_e_1)

    # Inspect weight data
    for i in range(32):
        for j in range(8):
            pylse.inspect(dr_weight_data[i][2*j], name=f"acc_dr_weight_data_{i}_bit_{j}_p")
            pylse.inspect(dr_weight_data[i][2*j + 1], name=f"acc_dr_weight_data_{i}_bit_{j}_n")

    ##########################################################################
    # Array of Processing Elements
    ##########################################################################

    # ofmap_out = pe_array(if_data, dr_weight_data, wrt_ctrl_pe, clks_dr[2])
    ofmap_out = pe_array(if_data, dr_weight_data, pylse.Wire(), clk_dr)

    # Connect the output of the PEs to the ifmap memory
    for i in range(8):
        for j in range(32):
            ofmap_in[i][j] <<= ofmap_out[i][j]

    return ofmap_out


def gen_inp_feat(input_features_ints):
    # Generate the PyLSE input signals given arrays of inputs at each clock cycle
    #   input_features_ints: 2D array of 8-bit integers, each row is an array of ints for each clock cycle
    
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
    # print(input_features_ints)
    # print(input_feats_bin)
    # input_feats_bin = transpose(input_feats_bin)
    # print(len(input_feats_bin))
    # print(len(input_feats_bin[0]))
    # print(len(input_feats_bin[0][0]))

    # print("Input features: ")
    # For each bit in the input feature number
    input_features = []
    for i in range(8):
        # print("Bit " + str(i) + ": ")
        pe_pulse_arr = []
        # For each input feature number for each PE
        for j in range(32):
            # print("int " + str(j) + ": ")
            # For each cycle
            pulses = []
            for k in range(len(input_feats_bin)):
                # print(input_feats_bin[k][j][i], end="")
                if input_feats_bin[k][j][i] == 1:
                    pulses.append(k*T)
                    # pulses.append(k*T + inp_delay)
                
            # print("")

            # Create the input signal
            inp_sig = pylse.inp_at(*pulses, name=f"input_feature_int{j}_bit{i}")
            pe_pulse_arr.append(inp_sig)
        input_features.append(pe_pulse_arr)
    

    # Print out the dimensions of the input signals
    # print("Dimensions of input signals:")
    # print("input_features: " + str(len(input_features)) + " x " + str(len(input_features[0])))
    
    return input_features

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

    # Print out dual rail clock cycles
    T = T/2
    num_cycles *= 2
    # For each cycle, ith cycle
    for i in range(num_cycles):

        print("CYCLE " + str(i) + ":")
        # For each PE, jth PE
        # For now just print out the first PE
        for j in range(1):
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
    T = 1200
    inp_delay = 100 + T
    num_cycles = 12
    clk = pylse.inp(start=T, period=T, n=num_cycles, name='clk')
    clk_e = pylse.inp(start=T + T/2, period=T, n=num_cycles, name='clk_e')
    clk_o = pylse.inp(start=T*2, period=T, n=num_cycles, name='clk_o')
    clk_dr = pylse.inp(start=T + T/2, period=T/2, n=num_cycles*2, name='clk_dr')
    
    # Give an early clock to the write control signal to write to the memories
    clk_wrt_ctrl = pylse.inp(start=0, period=T, n=num_cycles+1, name='clk_wrt_ctrl')

    # These are real input features from fnn_32.py
    # input_feats_init = [-8, -5, 8, 0, 8, 7, -2, 7, 9, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #                  0, 0, 0, 0, 0, 0, 0, 0]
    # Modified test inputs
    input_feats_init = [8, 5, 4, 2, 8, 7, -2, 7, 9, 7, 2, 4, 1, 5, 8, 2, 1, 0, 9, 7, 0, 5, 7, 2,
                     7, 2, 1, 9, 4, 3, 2, 8]
    # Flip the array
    input_feats_init = input_feats_init[::-1]

    zero_ins = [0 for i in range(32)]
    input_features_ints = [input_feats_init] + [zero_ins for i in range(num_cycles-1)]

    # Generate the inputs
    input_feature_pulses = gen_inp_feat(input_features_ints)

    # Generate the write control bits
    write_control_bits = [[0], [0], [0], [0], [0], [1]]

    # Generate some weights
    weights_set_one = [i for i in range(40)]
    weights_set_two = weights_set_one[::-1]

    weights_init = [weights_set_one for i in range(16)] + [weights_set_two for i in range(16)]

    # -- INSTANTIATE THE ACCELERATOR MODULE --
    nn_out = accelerator(input_feature_pulses, write_control_bits, weights_init, clk, clk_dr, clk_o, clk_e, clk_wrt_ctrl)

    # Probe outputs
    pylse.inspect(clk, 'clk')

    # Inspect the first PE output
    for i in range(8):
        pylse.inspect(nn_out[0][i], name=f"PE0_out_{i}")

    # Run Simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
    # sim.print_state()

    # Check outputs
    check_events(events, T, num_cycles)

    signal_list = ["clk", "clk_dr", "clk_o", "clk_e", "clk_wrt_ctrl"]
    # signal_list += ["acc_wrt_ctrl_bit"]
    # signal_list += [f"input_feature_int{i}_bit{j}" for i in range(32) for j in range(8)]
    signal_list += [f"PE0_out_{i}" for i in range(8)]
    signal_list += [f"acc_if_data_bit_{i}_p" for i in range(8)]
    signal_list += [f"acc_if_data_bit_{i}_n" for i in range(8)]
    signal_list += [f"acc_dr_weight_data_{i}_bit_{j}_p" for i in range(1) for j in range(8)]
    signal_list += [f"acc_dr_weight_data_{i}_bit_{j}_n" for i in range(1) for j in range(8)]
    signal_list += [f"acc_ofmap_in0_bit_{i}" for i in range(8)]

    print_events_trace(events, signal_list, until=15000, resolution=60, max_char=30)