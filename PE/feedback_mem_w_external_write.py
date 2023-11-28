"""
feedback_mem_w_external_write.py

This is a n-bit memory that writes back to itself every cycle but can be written a value with a signal.
"""

# imports
import pylse 

import shift_register



class Mux(pylse.SFQ):
    """ Synchronous Multiplexer

    This is the MUX from the PyLSE tutorial

    Emulates a multiplexer in SFQ, taking in four inputs (a, b, sel, and clk) and
    producing a single output (q).
    """

    name = 'MUX'
    inputs = ['a', 'b', 'sel', 'clk']
    outputs = ['q']

    transitions = [
        {'source': 'idle', 'trigger': 'a', 'dest': 'a_arrived', 'priority': 1},
        {'source': 'idle', 'trigger': 'b', 'dest': 'b_arrived', 'priority': 1},
        {'source': 'idle', 'trigger': 'sel', 'dest': 'sel_arrived', 'priority': 1},
        {'source': 'idle', 'trigger': 'clk', 'dest': 'idle', 'priority': 0},
        {'source': 'a_arrived', 'trigger': 'a', 'dest': 'a_arrived', 'priority': 1},
        {'source': 'a_arrived', 'trigger': 'b', 'dest': 'a_and_b_arrived', 'priority': 1},
        {'source': 'a_arrived', 'trigger': 'sel', 'dest': 'sel_arrived', 'priority': 1},
        {'source': 'a_arrived', 'trigger': 'clk', 'dest': 'idle', 'firing': 'q', 'priority': 0},
        {'source': 'b_arrived', 'trigger': 'a', 'dest': 'a_and_b_arrived', 'priority': 1},
        {'source': 'b_arrived', 'trigger': 'b', 'dest': 'b_arrived', 'priority': 1},
        {'source': 'b_arrived', 'trigger': 'sel', 'dest': 'b_and_sel_arrived', 'priority': 1},
        {'source': 'b_arrived', 'trigger': 'clk', 'dest': 'idle', 'priority': 0},
        {'source': 'a_and_b_arrived', 'trigger': ['a', 'b'], 'dest': 'a_and_b_arrived', 'priority': 1},
        {'source': 'a_and_b_arrived', 'trigger': 'sel', 'dest': 'b_and_sel_arrived', 'priority': 1},
        {'source': 'a_and_b_arrived', 'trigger': 'clk', 'dest': 'idle', 'firing': 'q', 'priority': 0},
        {'source': 'sel_arrived', 'trigger': ['a', 'sel'], 'dest': 'sel_arrived', 'priority': 1},
        {'source': 'sel_arrived', 'trigger': 'b', 'dest': 'b_and_sel_arrived', 'priority': 1},
        {'source': 'sel_arrived', 'trigger': 'clk', 'dest': 'idle', 'priority': 0},
        {'source': 'b_and_sel_arrived', 'trigger': ['a', 'b', 'sel'], 'dest': 'b_and_sel_arrived', 'priority': 1},
        {'source': 'b_and_sel_arrived', 'trigger': 'clk', 'dest': 'idle', 'firing': 'q', 'priority': 0}
    ]

    firing_delay = 5.0
    jjs = 15

def mux_s(a: pylse.Wire, b: pylse.Wire, sel: pylse.Wire, clk: pylse.Wire):
    out = pylse.Wire()
    pylse.working_circuit().add_node(Mux(), [a, b, sel, clk], [out])
    return out


def jtl(in0: pylse.Wire, out0: pylse.Wire, name=None, **overrides):
    pylse.working_circuit().add_node(pylse.sfq_cells.JTL(**overrides), [in0], [out0])
    return



def fb_mem_external_write(x_in, wrt, clk, n_bits):
    """
    Feedback memory with external write
    """

    # split out clk and wrt
    wrt_split = pylse.split(wrt, n_bits)
    clk_split = pylse.split(clk, n_bits)

    x_out = []
    for i in range(n_bits):
        mux_out_wire = pylse.Wire()
        fb_wire_delay = pylse.Wire()

        mux_out_wire = mux_s(fb_wire_delay, x_in[i], wrt_split[i], clk_split[i])
        mux_out_split = pylse.split(mux_out_wire, 2)
        jtl(mux_out_split[0],fb_wire_delay)

        x_out.append(mux_out_split[1])

    return x_out

def fb_mem_external_write_w_shift(x_in, wrt, clk, shift_len, n_bits):
    """
    Feedback memory with external write and a shift reg built in.

    # TODO add means of pausing the shifting
    """

    # split out clk and wrt
    wrt_split = pylse.split(wrt, n_bits)
    clk_split = pylse.split(clk, n_bits*2)

    x_out = []
    for i in range(n_bits):
        mux_out_wire = pylse.Wire()
        fb_wire_delay = pylse.Wire()

        mux_out_wire = mux_s(fb_wire_delay, x_in[i], wrt_split[i], clk_split[i*2])
        if shift_len > 1:
            sr_out_wire = shift_register.sr_single_bit(mux_out_wire, clk_split[(i*2)+1], shift_len-1)
        else:
            sr_out_wire = mux_out_wire
        sr_out_split = pylse.split(sr_out_wire, 2)
        jtl(sr_out_split[0],fb_wire_delay)

        x_out.append(sr_out_split[1])

    return x_out

def sr_single_bit_external_write(x_in, wrt, clk, sr_length):
    """
    circular shift register with external write in for all values
    """

    # Every bit is a mux and a splitter

    # split out clk and wrt
    wrt_split = pylse.split(wrt, sr_length)
    clk_split = pylse.split(clk, sr_length)

    x_out = []

    fb_wire_delay = pylse.Wire()
    temp_wires = []
    for i in range(sr_length):
        if i == 0:
            mux_out_wire = mux_s(fb_wire_delay, x_in[i], wrt_split[i], clk_split[i])
        else:
            mux_out_wire = mux_s(temp_wires[i-1], x_in[i], wrt_split[i], clk_split[i])
        sr_out_split = pylse.split(mux_out_wire, 2)
        temp_wires.append(sr_out_split[0])
        x_out.append(sr_out_split[1])
    jtl(temp_wires[-1],fb_wire_delay)

    return x_out

def sr_N_bit_external_write(x_in, wrt, clk, sr_length, n_bits):
    # The output
    x_out = []

    # Split the clk
    wrt_split = pylse.split(wrt, n_bits)
    clk_split = pylse.split(clk, n_bits)

    for i in range(n_bits):
        x_out.append(sr_single_bit_external_write(x_in[i], wrt_split[i], clk_split[i], sr_length))

    return x_out


if __name__ == "__main__":

    n_bits = 4
    shift_len = 3

    T = 80  # duration of a phase
    clk = pylse.inp(start=T/2, period=T, n=13, name='clk')

    # wrt = pylse.inp_at(T+1, 4*T+1, name='wrt')
    wrt = pylse.inp_at(T+1, 6*T+1, name='wrt')

    # Provided input at T == 1
    x_in = []
    for i in range(n_bits):
        if i == 0:
            x_in.append(pylse.inp(start=T, period=T, n=1, name=f'x_{i}'))
        if i == 1:
            x_in.append(pylse.inp(start=6*T, period=T, n=1, name=f'x_{i}'))
        else:
            x_in.append(pylse.inp(start=6*T, period=T, n=1, name=f'x_{i}'))

    # Call single_bit_sr()
    # x_out = fb_mem_external_write(x_in, wrt, clk, n_bits)
    # x_out = fb_mem_external_write_w_shift(x_in, wrt, clk, shift_len, n_bits)
    x_out = sr_single_bit_external_write(x_in, wrt, clk, n_bits)

    # Probe outputs
    pylse.inspect(clk, 'clk')
    for i in range(n_bits):
        pylse.inspect(x_in[i], f'x_in_{i}')
        pylse.inspect(x_out[i], f'x_out_{i}')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    # sim.print_state()
    sim.plot()

