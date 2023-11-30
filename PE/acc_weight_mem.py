import pylse

from helpers import *
from feedback_mem_w_external_write import sr_N_bit_external_write
from converters import alt_clock, sr_to_dr, dr_to_sr
from initialized_shift_register import create_sr_from_int_list_feedback

def s(x):
    return pylse.s(x, firing_delay=4.3)

def m(*args):
    return pylse.m(*args, firing_delay=8.2)

def weight_mem(weights_init, clk, clk_o, clk_e):
    """
    Weight Memory

    Inputs:
        weights_init: initial weights for the neural network
            Dimensions: 32 x N integer 2D array
        clk: clock signal
    
    Outputs:
        dr_weight_data_layers: 32 16-bit dual-railed int weights for each cycle
            Dimensions: 32 x 16-bit (dual-rail signal), consisting of 8 positive + 8 negative bits
    """

    # Split the clock signals
    clk_spl = pylse.split(clk, n=32, firing_delay=4.3)
    clk_o_spl = pylse.split(clk_o, n=32*8, firing_delay=4.3)
    clk_e_spl = pylse.split(clk_e, n=32*8, firing_delay=4.3)

    # Note that sr_weight_data_layers is single rail and needs to be converted to dual rail
    sr_weight_data = [create_sr_from_int_list_feedback(clk_spl[i], weights_init[i]) for i in range(32)]

    # Converts the single rail to dual rail
    # Dimensions are 32 x 8 x 2
    dr_weight_data_layers = []
    curr_clk_o_count = 0
    curr_clk_e_count = 0
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

    print("clock_o count:", curr_clk_o_count)
    print("clock_e count:", curr_clk_e_count)
    return dr_weight_data_layers

def check_events(events, T, num_cycles):
    print("Output:")

    print("Cycle Num | Cycle E | Cycle O | weight_out (pe 0 ... 31)")

    for i in range(num_cycles):
        print("Cycle " + str(i) + ":", end="")

        print(pulse_event_in_cycle(events, 'clk_e', T, i), end="|")
        print(pulse_event_in_cycle(events, 'clk_o', T, i), end="|")
        
        print("|", end="")

        # For each PE
        for j in range(32):
            print("[" + str(j) + "]", end="")
            bits = []
            for k in range(8):
                bit = pulse_event_in_cycle(events, f'weight_out_PE{j}_bit{k}_p', T, i)
                bits.append(bit)
                print(bit, end="")

            int_val = twos_to_dec(bits)
            print("=" + str(int_val), end="|")
        
        print("")
        
        
if __name__ == "__main__":
    T = 500
    num_cycles = 60
    clk = pylse.inp(start=T, period=T, n=num_cycles, name='clk')

    clk_o = pylse.inp(start=T*2, period=T*2, n=num_cycles, name='clk_o')
    clk_e = pylse.inp(start=T, period=T*2, n=num_cycles, name='clk_e')

    N_weights = 10

    # Generate some weights
    weights_set_one = [i for i in range(N_weights)]
    weights_set_two = weights_set_one[::-1]

    weights_init = [weights_set_one for i in range(16)] + [weights_set_two for i in range(16)]

    weight_data_out = weight_mem(weights_init, clk, clk_o, clk_e)

    # pylse.inspect(clk1, 'clk')
    pylse.inspect(clk_o, 'clk_o')
    pylse.inspect(clk_e, 'clk_e')
    
    # Inspect the output bits
    for i in range(32):
        # For every output number

        # Inspect the positive bits
        for j in range(8):
            pylse.inspect(weight_data_out[i][j], f"weight_out_PE{i}_bit{j}_p")
        
        for j in range(8, 16):
            pylse.inspect(weight_data_out[i][j], f"weight_out_PE{i}_bit{j}_n")

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Check outputs
    check_events(events, T, num_cycles)