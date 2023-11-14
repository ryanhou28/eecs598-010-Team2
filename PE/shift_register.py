"""
shift_register.py

Make some parametrized shift registers.
"""

# imports
import pylse 


# Define some helpers

def s(x):
    """
    Splitter
    """
    return pylse.s(x, firing_delay=4.3)

def dro(*args):
    """
    Destructive readout
    """
    return pylse.dro(*args, firing_delay=5.1)

def dro_pair(x, clk):
    """
    xSFQ storage element consisting of two DRO cells in series.
    """
    return dro(pylse.jtl(dro(pylse.jtl(x), clk[0])), clk[1])

def sr_single_bit_recursive(x, clk, length):
    """
    A parametric shift register. Many dro's in series

    TODO find a better way than recursive
    """

    if length == 1:
        return dro(pylse.jtl(x), clk[0])
    else:
        return dro(pylse.jtl(sr_single_bit_recursive(x,clk,length-1)), clk[length-1])

def sr_single_bit(x, clk, length):
    """
    A parametric shift register. Many dro's in series

    TODO find a better way than recursive
    """

    clk_fo = pylse.split(clk, length)

    return sr_single_bit_recursive(x, clk_fo, length)
    
def sr_N_bit(x, clk, length, n_bits):
    """
    A stack of parametric shift register. Many dro's in series.
    """

    # The output
    x_out = []

    # Split the clk
    clk_split = pylse.split(clk, n_bits)

    for i in range(n_bits):
        x_out.append(sr_single_bit(x[i], clk_split[i], length))

    return x_out


if __name__ == "__main__":

    T = 80  # duration of a phase
    clk = pylse.inp(start=T/2, period=T, n=10, name='clk')

    # Provided input: a=1, b=1, cin=0
    x_2 = pylse.inp_at(0*T, name='a_p')

    # Call single_bit_sr()
    x_out = sr_single_bit(x_2, clk, 4)

    # Probe outputs
    pylse.inspect(clk, 'clk')
    pylse.inspect(x_2, 'x_2')
    pylse.inspect(x_out, 'x_out')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()