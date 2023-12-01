"""
accelerator_area_analysis.py

We want to look at the jj count and area of the components
"""

# imports
import pylse

# local imports
from helpers import *
from processing_element_8bit import processing_element
from feedback_mem_w_external_write import sr_N_bit_external_write, mux_s
from initialized_shift_register import create_sr_from_init_states, create_sr_from_int_list
from converters import alt_clock, sr_to_dr, dr_to_sr

##########################################################################
# Define xSFQ cells needed
##########################################################################

def m(*args):
    return pylse.m(*args, firing_delay=8.2)

def s(x):
    return pylse.s(x, firing_delay=4.3)


##########################################################################
# Write Control Memory
##########################################################################

def write_control_memory(clk, N_num_cycles):
    """
    """

    # TODO: This is just a placeholder for now, add actual control signal!
    write_control_bits = [[1] for i in range(N_num_cycles)] 

    control_mem_in = pylse.Wire()

    control_mem = create_sr_from_init_states([control_mem_in], clk, write_control_bits)

    return control_mem


##########################################################################
# Input Feature Memory
##########################################################################

def input_feature_memory(clk, clk_o, clk_e):

    wrt_ctrl = pylse.Wire()

    # Split the clock signal
    clk_o_spl = pylse.split(clk_o, n=8, firing_delay=4.3)
    clk_e_spl = pylse.split(clk_e, n=8, firing_delay=4.3)

    N_PE = 32

    input_features = [[pylse.Wire() for i in range(8)] for j in range(32)]

    # Input Feature Memory will consist of 1 array of 8-bit wide 32 stages deep shift registers

    # Instantiate wires for input to the ifmap memory
    ofmap_in = [[pylse.Wire() for i in range(8)] for j in range(N_PE)]

    # Merge the input feature and the input from psums 
    # The merger essentially acts as a mux to select between input features and ofmap
    # This assumes the psums are initialized to 0s and that the input feature comes in at the first cycle
    if_mem_in = [[m(input_features[i][j], ofmap_in[i][j]) for i in range(N_PE)] for j in range(8)]

    if_data_sr = sr_N_bit_external_write(if_mem_in, wrt_ctrl, clk, N_PE, 8)

    # Convert the single rail output to dual rail
    p_list = []
    n_list = []
    for i in range(8):
        if_p, if_n = sr_to_dr(if_data_sr[i], clk_o_spl[i], clk_e_spl[i])
        p_list.append(if_p)
        n_list.append(if_n)
    if_data = p_list + n_list

    # Split the if_data 32 ways to each PE
    if_data_spl = [pylse.split(if_data[i], n=N_PE, firing_delay=4.3) for i in range(16)]

    # Transpose the split if_data for easier indexing
    if_data_spl = [list(row) for row in zip(*if_data_spl)]
    
##########################################################################
# Weight Memory
##########################################################################

def weight_memory(clk, clk_o, clk_e):

    N_PE = 32
    N_num_cycles = 4 * 32

    N_clocks = 32
    N_clocks_o = 32 * 8
    N_clocks_e = 32 * 8

    curr_clk_o_count = 0
    curr_clk_e_count = 0

    clk_spl = pylse.split(clk, n=N_clocks, firing_delay=4.3)
    clk_o_spl = pylse.split(clk_o, n=N_clocks_o, firing_delay=4.3)
    clk_e_spl = pylse.split(clk_e, n=N_clocks_e, firing_delay=4.3)

    # TODO: This is just a placeholder for now, add actual control signal!
    # Note that this is a single rail memory 8bits * N-num_cycles * N_PE
    weight_init_states = [[[0 for i in range(8)] for j in range(N_num_cycles)] for k in range(N_PE)] 

    # Create wires for feedback input to the weight memory
    weight_mem_in = [[pylse.Wire() for i in range(8)] for k in range(N_PE)]

    # Note that sr_weight_data_layers is single rail and needs to be converted to dual rail
    sr_weight_data_layers = [create_sr_from_init_states(weight_mem_in[i], clk_spl[i], weight_init_states[i]) for i in range(N_PE)]

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

    # print(curr_clk_o_count)
    # print(curr_clk_e_count)

    return dr_weight_data_layers

##########################################################################
# Array of Processing Elements
##########################################################################

def processing_element_array(clk):

    N_PE = 32
    N_clocks = N_PE + 16 * N_PE
    curr_clk_count = 0

    # Split the clock signal
    clk_spl = pylse.split(clk, n=N_clocks, firing_delay=4.3)

    # Split the reset signal
    # fanout for the ifmap and the psum buffers in the PEs
    wrt_ctrl_spl = pylse.split(pylse.Wire(), n=N_PE, firing_delay=4.3)

    if_data_spl = [[pylse.Wire() for i in range(16)] for j in range(N_PE)]

    dr_weight_data_layers = [[pylse.Wire() for i in range(16)] for j in range(N_PE)]

    pe_out = [processing_element(if_data_spl[i], dr_weight_data_layers[i], wrt_ctrl_spl[i], clk_spl[curr_clk_count + i]) for i in range(N_PE)]

    curr_clk_count += N_PE

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

    return split_inverted_delayed_pe_out

##########################################################################
# The whole accelerator
##########################################################################

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
    N_num_cycles = 4 * 32 # TODO: Update this with the actual number of total clock cycles needed
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
    # TODO: This is just a placeholder for now, add actual control signal!
    write_control_bits = [[1] for i in range(N_num_cycles)] 

    control_mem_in = pylse.Wire()

    control_mem = create_sr_from_init_states([control_mem_in], clk_spl[curr_clk_count], write_control_bits)
    curr_clk_count += 1

    control_mem_in = control_mem[0]

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

def analysis_write_control_memory():

    T = 1000
    num_cycles = 5
    clk = pylse.inp(start=T/2, period=T, n=num_cycles, name='clk')

    out = write_control_memory(clk, 4*32)

    sim = pylse.Simulation()
    events = sim.simulate()
    # sim.plot()
    sim.print_state()

def analysis_weight_memory():

    T = 1000
    num_cycles = 5
    clk = pylse.inp(start=T/2, period=T, n=num_cycles, name='clk')
    clk_e = pylse.inp(start=T/2, period=T*2, n=num_cycles, name='clk_e')
    clk_o = pylse.inp(start=T/2+T*2, period=T*2, n=num_cycles, name='clk_o')

    out = weight_memory(clk, clk_o, clk_e)

    sim = pylse.Simulation()
    events = sim.simulate()
    # sim.plot()
    sim.print_state()

def analysis_input_feature_memory():

    T = 1000
    num_cycles = 5
    clk = pylse.inp(start=T/2, period=T, n=num_cycles, name='clk')
    clk_e = pylse.inp(start=T/2, period=T*2, n=num_cycles, name='clk_e')
    clk_o = pylse.inp(start=T/2+T*2, period=T*2, n=num_cycles, name='clk_o')

    out = input_feature_memory(clk, clk_o, clk_e)

    sim = pylse.Simulation()
    events = sim.simulate()
    # sim.plot()
    sim.print_state()

def analysis_processing_element_array():

    T = 1000
    num_cycles = 5
    clk = pylse.inp(start=T/2, period=T, n=num_cycles, name='clk')

    processing_element_array(clk)

    sim = pylse.Simulation()
    events = sim.simulate()
    # sim.plot()
    sim.print_state()

def test_single_input(input_feature_bin_arr):
    # Test a single input
    T = 1000

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

def analysis_accelerator():
    """
    """

    T = 1000
    num_cycles = 1
    clk = pylse.inp(start=T/2, period=T, n=num_cycles, name='clk')
    clk_e = pylse.inp(start=T/2, period=T*2, n=num_cycles, name='clk_e')
    clk_o = pylse.inp(start=T/2+T*2, period=T*2, n=num_cycles, name='clk_o')
    
    input_features = [0 for i in range(32)]
    
    input_feature_bin = [twos_complement_bin(input_features[i]) for i in range(len(input_features))]

    # Print out the input features
    print("Input Features:")
    print(input_features)

    # Generate the inputs
    input_features_pulses = test_single_input(input_feature_bin)

    nn_out, wrt_ctrl_out, pe_out  = accelerator(input_features_pulses, clk, clk_o, clk_e)

    sim = pylse.Simulation()
    events = sim.simulate()
    # sim.plot()
    sim.print_state()

if __name__ == "__main__":
    
    # analysis_write_control_memory()
    # analysis_weight_memory()
    # analysis_input_feature_memory()
    # analysis_processing_element_array()
    analysis_accelerator()