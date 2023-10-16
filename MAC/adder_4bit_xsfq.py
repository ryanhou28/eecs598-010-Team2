import pylse
from helpers import BaseTest, sim_and_gen, pulse_in_period
from full_adder_xsfq import full_adder_xSFQ
import unittest

# Define the adder
def adder_4bit(a_p, a_n, b_p, b_n, cin_p, cin_n):

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

    # Split cin
    cin_p0, cin_p1 = s(cin_p)
    cin_n0, cin_n1 = s(cin_n)

    c_p = [0, 0, 0, 0]
    c_n = [0, 0, 0, 0]
    s_p = [0, 0, 0, 0]
    s_n = [0, 0, 0, 0]
    for i in range(0, 4):
        if (i == 0):
            spi, sni, cpi, cpn = full_adder_xSFQ(a_p[i], a_n[i], b_p[i], b_n[i], cin_p0, cin_n0)
        else:
            spi, sni, cpi, cpn = full_adder_xSFQ(a_p[i], a_n[i], b_p[i], b_n[i], c_p[i-1], c_n[i-1])

        s_p[i] = spi
        s_n[i] = sni
        c_p[i] = cpi
        c_n[i] = cpn
    
    return s_p, s_n, c_p[3], c_n[3]


def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def test_single_input(a3, a2, a1, a0, b3, b2, b1, b0):
    a0_p_t = inv(a0)
    a0_n_t = a0
    a1_p_t = inv(a1)
    a1_n_t = a1
    a2_p_t = inv(a2)
    a2_n_t = a2
    a3_p_t = inv(a3)
    a3_n_t = a3
    b0_p_t = inv(b0)
    b0_n_t = b0
    b1_p_t = inv(b1)
    b1_n_t = b1
    b2_p_t = inv(b2)
    b2_n_t = b2
    b3_p_t = inv(b3)
    b3_n_t = b3

    a0_p = pylse.inp_at(a0_p_t*T, name='a0_p')
    a0_n = pylse.inp_at(a0_n_t*T, name='a0_n')
    a1_p = pylse.inp_at(a1_p_t*T, name='a1_p')
    a1_n = pylse.inp_at(a1_n_t*T, name='a1_n')
    a2_p = pylse.inp_at(a2_p_t*T, name='a2_p')
    a2_n = pylse.inp_at(a2_n_t*T, name='a2_n')
    a3_p = pylse.inp_at(a3_p_t*T, name='a3_p')
    a3_n = pylse.inp_at(a3_n_t*T, name='a3_n')
    b0_p = pylse.inp_at(b0_p_t*T, name='b0_p')
    b0_n = pylse.inp_at(b0_n_t*T, name='b0_n')
    b1_p = pylse.inp_at(b1_p_t*T, name='b1_p')
    b1_n = pylse.inp_at(b1_n_t*T, name='b1_n')
    b2_p = pylse.inp_at(b2_p_t*T, name='b2_p')
    b2_n = pylse.inp_at(b2_n_t*T, name='b2_n')
    b3_p = pylse.inp_at(b3_p_t*T, name='b3_p')
    b3_n = pylse.inp_at(b3_n_t*T, name='b3_n')

    a_p = [a0_p, a1_p, a2_p, a3_p]
    a_n = [a0_n, a1_n, a2_n, a3_n]
    b_p = [b0_p, b1_p, b2_p, b3_p]
    b_n = [b0_n, b1_n, b2_n, b3_n]

    # Return a zero input for carry in
    zero_p_t = inv(0)
    zero_n_t = 0
    zero_p = pylse.inp_at(zero_p_t*T, name='zero_p')
    zero_n = pylse.inp_at(zero_n_t*T, name='zero_n')

    return a_p, a_n, b_p, b_n, zero_p, zero_n


def check_events(events, T):
    print(int(events['cout_p'][0] < T), int(events['s3_p'][0] < T), int(events['s2_p'][0] < T), int(events['s1_p'][0] < T), int(events['s0_p'][0] < T))

if __name__ == "__main__":

    T = 320 # duration of a phase

    # Test input
    a_p, a_n, b_p, b_n, zero_p, zero_n = test_single_input(1, 0, 1, 0, 1, 0, 1, 1)

    # Instantiate the multiplier
    s_p, s_n, c_p, c_n = adder_4bit(a_p, a_n, b_p, b_n, zero_p, zero_n)

    s0_p, s1_p, s2_p, s3_p = s_p
    s0_n, s1_n, s2_n, s3_n = s_n

    # Probe outputs
    pylse.inspect(s0_p, 's0_p')
    pylse.inspect(s0_n, 's0_n')
    pylse.inspect(s1_p, 's1_p')
    pylse.inspect(s1_n, 's1_n')
    pylse.inspect(s2_p, 's2_p')
    pylse.inspect(s2_n, 's2_n')
    pylse.inspect(s3_p, 's3_p')
    pylse.inspect(s3_n, 's3_n')
    pylse.inspect(c_p, 'cout_p')
    pylse.inspect(c_n, 'cout_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()


    # Print out the events
    check_events(events, T)