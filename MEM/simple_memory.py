"""
simple_memory.py
"""

# imports
import pylse 


def simple_mem_N_bit(x_in, rst, clk, n_bits):
    """
    This is the simple memory for the accumulate loop.
    
    """

    x_out = []
    rst_split = pylse.split(rst, n_bits)
    clk_split = pylse.split(clk, n_bits)

    for i in range(n_bits):
        x_out.append(pylse.dro_sr(x_in[i], clk_split[i], rst_split[i]))

    return x_out

if __name__ == "__main__":

    n_bits = 4

    T = 80  # duration of a phase
    clk = pylse.inp(start=T/2, period=T, n=8, name='clk')

    rst = pylse.inp_at(4*T, name='rst')

    # Provided input at T == 1
    x_in = []
    for i in range(n_bits):
        x_in.append(pylse.inp(start=T, period=T, n=5, name=f'x_{i}'))

    # Call single_bit_sr()
    x_out = simple_mem_N_bit(x_in, clk, rst, n_bits)

    # Probe outputs
    pylse.inspect(clk, 'clk')
    for i in range(n_bits):
        pylse.inspect(x_in[i], f'x_in_{i}')
        pylse.inspect(x_out[i], f'x_out_{i}')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()