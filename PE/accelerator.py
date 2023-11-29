import pylse

from processing_element_8bit import processing_element
from feedback_mem_w_external_write import sr_single_bit_external_write
from initialized_shift_register import create _sr_from_init_states, create_sr_from_int_list

def accelerator(clk):
    # Define constants
    N_PE = 32
    N_clocks = 32 # TODO: Update this with the actual number of clock splits needed
    N_resets = 32 # TODO: Update this with the actual number of reset splits needed
    N_num_cycles = 32 # TODO: Update this with the actual number of totol clock cycles needed

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
    write_control_bits = [0, 1, 0, 1, 0, 1, 0, 1] # TODO: This is just a placeholder for now, add actual control signal!

    control_mem = create_sr_from_int_list(pylse.Wire(), clk, write_control_bits)

    curr_rst_count = 0

    # TODO: Fill in the connections between the write control memory and the processing elements
    rest = ...

    # Split the reset signal
    rst_spl = pylse.split(reset, n=N_resets, firing_delay=4.3)
    # TODO: Rename "reset" to "write_ctrl" or a more intuitive name

    ##########################################################################
    # Input Feature Memory
    ##########################################################################

    # Input Feature Memory will consist of 2 arrays of 8-bit wide 16 stages deep shift registers
    #  One array will be the positive pulses for input feature memory, and the other containing the negative values
    #  Both arrays need to be 2 * 8 = 16 stages deep due to alternating phases of xSFQ 

    if_mem_p = sr_N_bit_external_write(pylse.Wire(), rst_spl[curr_rst_count + i], clk_spl[curr_clk_count], N_PE, 16)
    curr_clk_count += 1
    curr_rst_count += 1

    if_mem_n = sr_N_bit_external_write(pylse.Wire(), rst_spl[curr_rst_count + i], clk_spl[curr_clk_count], N_PE, 16)
    curr_clk_count += 1
    curr_rst_count += 1

    # TODO: Fill in the connections between the processing elements and the input feature memory
    if_data = ...

    ##########################################################################
    # Weight Memory
    ##########################################################################

    weight_init_states = [[0 for i in range(8)] for i in range(32) + [1 for i in range(8)] for i in range(32)] # TODO: This is just a placeholder for now, add actual control signal!

    # Weight memory is an array of 32 16-bit wide shift registers
    #   16-bit due to 8-bit positive and 8-bit negative pulses for each weight

    weight_mem = create_sr_from_init_states(pylse.Wire(), clk_spl[curr_clk_count], weight_init_states)
    curr_clk_count += 1

    # TODO: Fill in connections between the weight memory and the processing elements
    weight_data = ...

    ##########################################################################
    # Array of Processing Elements
    ##########################################################################

    pe_out = [processing_element(if_data[i], weight_data[i], rst_spl[i], clk_spl[i]) for i in range(N_PE)]

    curr_clk_count += N_PE
    curr_rst_count += N_PE

    # NOTE: pe_out is structured as an array of 8 wires, where all but the last wire (MSB) are inverted values
    #           so we need to invert the values to get the correct output when connecting to the memories

return nn_out



if __name__ == "__main__":
    # Define clock period
    T = 500
    clk = pylse.inp(start=T/2, period=T, n=10, name='clk')

    pe_out = accelerator(clk)

    # Probe outputs
    pylse.inspect(clk, 'clk')
    # TODO: Add probes for each output

    # Run Simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Check outputs
    # TODO