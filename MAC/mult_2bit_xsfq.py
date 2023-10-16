import pylse
from helpers import BaseTest, sim_and_gen, pulse_in_period

import unittest

# Define the multiplier
def mult_2bit(a0_p, a0_n, a1_p, a1_n, b0_p, b0_n, b1_p, b1_n):
    # c3c2c1c0 = a1a0 * b1b0

    # Define helpers to ensure same delay numbers (currently the same as PyLSE example)
    def jtl(*args):
        return pylse.jtl(*args, firing_delay=5.7)

    def fa(x, y):
        """ First-arrival cell based on an inverted C-element.
            Inputs buffered with JTL for better flux transmission.
        """
        return pylse.c_inv(jtl(x), jtl(y), firing_delay=9.0)

    def la(x, y):
        """ Last-arrival cell based on a C-element.
            Inputs buffered with JTL for better flux transmission.
        """
        return pylse.c(jtl(x), jtl(y), firing_delay=8.0)

    def s(x):
        return pylse.s(x, firing_delay=4.3)

    def dro(*args):
        return pylse.dro(*args, firing_delay=5.1)

    # Define the actual hardware
    #   FA -> OR
    #   LA -> AND

    # Split the first layer of inputs
    a0_p0, a0_p1 = s(a0_p)
    a0_n0, a0_n1 = s(a0_n)
    b0_p0, b0_p1 = s(b0_p)
    b0_n0, b0_n1 = s(b0_n)
    a1_p0, a1_p1 = s(a1_p)
    a1_n0, a1_n1 = s(a1_n)
    b1_p0, b1_p1 = s(b1_p)
    b1_n0, b1_n1 = s(b1_n)

    # First layer of ANDs

    # AND1
    and1_p = la(a0_p0, b1_p0)
    and1_n = fa(a0_n0, b1_n0)

    # AND2
    and2_p = la(a0_p1, b0_p0)
    and2_n = fa(a0_n1, b0_n0)

    # AND3
    and3_p = la(a1_p0, b0_p1)
    and3_n = fa(a1_n0, b0_n1)

    # AND4
    and4_p = la(a1_p1, b1_p1)
    and4_n = fa(a1_n1, b1_n1)

    # Split the outputs of the first layer of ANDs
    and1_p0s0, and1_p0s1 = s(and1_p)
    and1_p0, and1_p1 = s(and1_p0s0)
    and1_p2, and1_p3 = s(and1_p0s1)

    and1_n0s0, and1_n0s1 = s(and1_n)
    and1_n0, and1_n1 = s(and1_n0s0)
    and1_n2, and1_n3 = s(and1_n0s1)

    and2_p0s0, and2_p0s1 = s(and2_p)
    and2_p0, and2_p1 = s(and2_p0s0)
    and2_p2, and2_p3 = s(and2_p0s1)

    and2_n0s0, and2_n0s1 = s(and2_n)
    and2_n0, and2_n1 = s(and2_n0s0)
    and2_n2, and2_n3 = s(and2_n0s1)

    and3_p0s0, and3_p0s1 = s(and3_p)
    and3_p0, and3_p1 = s(and3_p0s0)
    and3_p2, and3_p3 = s(and3_p0s1)

    and3_n0s0, and3_n0s1 = s(and3_n)
    and3_n0, and3_n1 = s(and3_n0s0)
    and3_n2, and3_n3 = s(and3_n0s1)

    and4_p0s0, and4_p0s1 = s(and4_p)
    and4_p0, and4_p1 = s(and4_p0s0)
    and4_p2, and4_p3 = s(and4_p0s1)

    and4_n0s0, and4_n0s1 = s(and4_n)
    and4_n0, and4_n1 = s(and4_n0s0)
    and4_n2, and4_n3 = s(and4_n0s1)

    # XOR1
    xor1_p_and1 = la(and1_n0, and3_p0)
    xor1_p_and2 = la(and1_p0, and3_n0)
    xor1_p = fa(xor1_p_and1, xor1_p_and2)

    xor_1_n_and1 = la(and1_p1, and3_p1)
    xor_1_n_and2 = la(and1_n1, and3_n1)
    xor1_n = fa(xor_1_n_and1, xor_1_n_and2)

    # AND5
    and5_p = la(and1_p2, and3_p2)
    and5_n = fa(and1_n2, and3_n2)

    # Split AND5
    and5_ps0, and5_ps1 = s(and5_p)
    and5_p0, and5_p1 = s(and5_ps0)
    and5_p2, and5_p3 = s(and5_ps1)

    and5_ns0, and5_ns1 = s(and5_n)
    and5_n0, and5_n1 = s(and5_ns0)
    and5_n2, and5_n3 = s(and5_ns1)

    # AND6
    and6_p = la(and5_p0, and4_p0)
    and6_n = fa(and5_n0, and4_n0)

    # XOR2
    xor2_p_and1 = la(and5_n1, and4_p1)
    xor2_p_and2 = la(and5_p1, and4_n1)
    xor2_p = fa(xor2_p_and1, xor2_p_and2)

    xor2_n_and1 = la(and5_p2, and4_p2)
    xor2_n_and2 = la(and5_n2, and4_n2)
    xor2_n = fa(xor2_n_and1, xor2_n_and2)

    # Connect the outputs
    c0_p = and2_p
    c0_n = and2_n

    c1_p = xor1_p
    c1_n = xor1_n

    c2_p = xor2_p
    c2_n = xor2_n

    c3_p = and6_p
    c3_n = and6_n

    return c0_p, c0_n, c1_p, c1_n, c2_p, c2_n, c3_p, c3_n


def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def test_single_input(a0, a1, b0, b1):
    a0_p_t = inv(a0)
    a0_n_t = a0
    a1_p_t = inv(a1)
    a1_n_t = a1
    b0_p_t = inv(b0)
    b0_n_t = b0
    b1_p_t = inv(b1)
    b1_n_t = b1

    a0_p = pylse.inp_at(a0_p_t*T, name='a0_p')
    a0_n = pylse.inp_at(a0_n_t*T, name='a0_n')
    a1_p = pylse.inp_at(a1_p_t*T, name='a1_p')
    a1_n = pylse.inp_at(a1_n_t*T, name='a1_n')
    b0_p = pylse.inp_at(b0_p_t*T, name='b0_p')
    b0_n = pylse.inp_at(b0_n_t*T, name='b0_n')
    b1_p = pylse.inp_at(b1_p_t*T, name='b1_p')
    b1_n = pylse.inp_at(b1_n_t*T, name='b1_n')

    return a0_p, a0_n, a1_p, a1_n, b0_p, b0_n, b1_p, b1_n

if __name__ == "__main__":

    T = 320 # duration of a phase

    # Test input
    a0_p, a0_n, a1_p, a1_n, b0_p, b0_n, b1_p, b1_n = test_single_input(1, 1, 1, 1)

    # Instantiate the multiplier
    c0_p, c0_n, c1_p, c1_n, c2_p, c2_n, c3_p, c3_n = mult_2bit(a0_p, a0_n, a1_p, a1_n, b0_p, b0_n, b1_p, b1_n)

    # Probe outputs
    pylse.inspect(c0_p, 'c0_p')
    pylse.inspect(c0_n, 'c0_n')
    pylse.inspect(c1_p, 'c1_p')
    pylse.inspect(c1_n, 'c1_n')
    pylse.inspect(c2_p, 'c2_p')
    pylse.inspect(c2_n, 'c2_n')
    pylse.inspect(c3_p, 'c3_p')
    pylse.inspect(c3_n, 'c3_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()