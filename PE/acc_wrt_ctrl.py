import pylse

from initialized_shift_register import create_sr_from_init_states

def write_control_mem(write_control_bits, clk):
    """
    Write control memory
    """

    control_mem_in = pylse.Wire()

    control_mem = create_sr_from_init_states([control_mem_in], clk, write_control_bits)

    control_mem_in = control_mem[0]

    return control_mem[0]

def check_events(events, T, num_cycles):
    print("Output:")

    for i in range(num_cycles):

        print("Cycle " + str(i) + ":", end=" ")
        pulse_this_cycle = False
        # For each event in this wire
        for j in range(len(events['control_mem_out'])):
            if events['control_mem_out'][j] < i*T and events['control_mem_out'][j] >= (i-1)*T:
                print("1")
                pulse_this_cycle = True
                break
        if not pulse_this_cycle:
            print("0")
    
        
if __name__ == "__main__":
    T = 500
    num_cycles = 12
    clk = pylse.inp(start=T, period=T, n=num_cycles, name='clk')

    write_control_bits = [[1], [1], [0], [0], [0], [0]]
    N_bits = len(write_control_bits)

    control_mem_out = write_control_mem(write_control_bits, clk)

    pylse.inspect(clk, 'clk')

    pylse.inspect(control_mem_out, 'control_mem_out')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Check outputs
    check_events(events, T, num_cycles)