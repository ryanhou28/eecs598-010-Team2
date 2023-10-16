import pylse
from helpers import BaseTest, sim_and_gen, pulse_in_period
from full_adder_xsfq import full_adder_xSFQ
from half_adder_xsfq import half_adder
from adder_4bit_xsfq import adder_4bit

import unittest

# Define the multiplier
def mult_4bit(x_p_in, x_n_in, y_p_in, y_n_in, zero_p, zero_n):
    # 4-bit unsigned combinational multiplier
    # Reference Design: https://i.stack.imgur.com/kPaLO.png

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

    def and_xsfq(x_p, x_n, y_p, y_n):
        # Get the outputs to the AND gate
        and_p = la(x_p, y_p)
        and_n = fa(x_n, y_n)

        return and_p, and_n


    # Define the actual hardware
    #   FA -> OR
    #   LA -> AND

    # Split the zero input
    zero_ps0, zero_ps1 = s(zero_p)
    zero_ns0, zero_ns1 = s(zero_n)
    zero_p0, zero_p1 = s(zero_ps0)
    zero_n0, zero_n1 = s(zero_ns0)
    zero_p2, zero_p3 = s(zero_ps1)
    zero_n2, zero_n3 = s(zero_ns1)

    # Split the inputs to a 2D array
    x_p_1 = []
    x_n_1 = []
    y_p_1 = []
    y_n_1 = []
    x_p_2 = []
    x_n_2 = []
    y_p_2 = []
    y_n_2 = []
    x_p_3 = []
    x_n_3 = []
    y_p_3 = []
    y_n_3 = []
    x_p_4 = []
    x_n_4 = []
    y_p_4 = []
    y_n_4 = []
    for i in range(len(x_p_in)):
        x_ps0, x_ps1 = s(x_p_in[i])
        x_ns0, x_ns1 = s(x_n_in[i])
        y_ps0, y_ps1 = s(y_p_in[i])
        y_ns0, y_ns1 = s(y_n_in[i])

        x_p_1_i, x_p_2_i = s(x_ps0)
        x_n_1_i, x_n_2_i = s(x_ns0)
        y_p_1_i, y_p_2_i = s(y_ps0)
        y_n_1_i, y_n_2_i = s(y_ns0)

        x_p_3_i, x_p_4_i = s(x_ps1)
        x_n_3_i, x_n_4_i = s(x_ns1)
        y_p_3_i, y_p_4_i = s(y_ps1)
        y_n_3_i, y_n_4_i = s(y_ns1)

        x_p_1.append(x_p_1_i)
        x_n_1.append(x_n_1_i)
        y_p_1.append(y_p_1_i)
        y_n_1.append(y_n_1_i)

        x_p_2.append(x_p_2_i)
        x_n_2.append(x_n_2_i)
        y_p_2.append(y_p_2_i)
        y_n_2.append(y_n_2_i)

        x_p_3.append(x_p_3_i)
        x_n_3.append(x_n_3_i)
        y_p_3.append(y_p_3_i)
        y_n_3.append(y_n_3_i)

        x_p_4.append(x_p_4_i)
        x_n_4.append(x_n_4_i)
        y_p_4.append(y_p_4_i)
        y_n_4.append(y_n_4_i)

    x_p = [x_p_1, x_p_2, x_p_3, x_p_4]
    x_n = [x_n_1, x_n_2, x_n_3, x_n_4]
    y_p = [y_p_1, y_p_2, y_p_3, y_p_4]
    y_n = [y_n_1, y_n_2, y_n_3, y_n_4]
    
    z_p = [0, 0, 0, 0, 0, 0, 0, 0]
    z_n = [0, 0, 0, 0, 0, 0, 0, 0]

    z_p[0], z_n[0] = and_xsfq(x_p[0][0], x_n[0][0], y_p[0][0], y_n[0][0])

    # First layer of ANDs
    adder1_b0_p, adder1_b0_n = and_xsfq(x_p[0][1], x_n[0][1], y_p[1][0], y_n[1][0])
    adder1_b1_p, adder1_b1_n = and_xsfq(x_p[0][2], x_n[0][2], y_p[2][0], y_n[2][0])
    adder1_b2_p, adder1_b2_n = and_xsfq(x_p[0][3], x_n[0][3], y_p[3][0], y_n[3][0])

    adder1_a0_p, adder1_a0_n = and_xsfq(x_p[1][0], x_n[1][0], y_p[0][1], y_n[0][1])
    adder1_a1_p, adder1_a1_n = and_xsfq(x_p[1][1], x_n[1][1], y_p[1][1], y_n[1][1])
    adder1_a2_p, adder1_a2_n = and_xsfq(x_p[1][2], x_n[1][2], y_p[2][1], y_n[2][1])
    adder1_a3_p, adder1_a3_n = and_xsfq(x_p[1][3], x_n[1][3], y_p[3][1], y_n[3][1])

    adder1_a_p = [adder1_a0_p, adder1_a1_p, adder1_a2_p, adder1_a3_p]
    adder1_a_n = [adder1_a0_n, adder1_a1_n, adder1_a2_n, adder1_a3_n]

    adder1_b_p = [adder1_b0_p, adder1_b1_p, adder1_b2_p, zero_p0]
    adder1_b_n = [adder1_b0_n, adder1_b1_n, adder1_b2_n, zero_n0]

    # First Adder
    adder1_s_p, adder1_s_n, adder1_c_p, adder1_c_n = adder_4bit(adder1_a_p, adder1_a_n, adder1_b_p, adder1_b_n, zero_p1, zero_n1)

    z_p[1], z_n[1] = adder1_s_p[0], adder1_s_n[0]

    adder2_b_p = [adder1_s_p[1], adder1_s_p[2], adder1_s_p[3], adder1_c_p]
    adder2_b_n = [adder1_s_n[1], adder1_s_n[2], adder1_s_n[3], adder1_c_n]

    # Second layer of ANDs
    adder2_a0_p, adder2_a0_n = and_xsfq(x_p[2][0], x_n[2][0], y_p[0][2], y_n[0][2])
    adder2_a1_p, adder2_a1_n = and_xsfq(x_p[2][1], x_n[2][1], y_p[1][2], y_n[1][2])
    adder2_a2_p, adder2_a2_n = and_xsfq(x_p[2][2], x_n[2][2], y_p[2][2], y_n[2][2])
    adder2_a3_p, adder2_a3_n = and_xsfq(x_p[2][3], x_n[2][3], y_p[3][2], y_n[3][2])

    adder2_a_p = [adder2_a0_p, adder2_a1_p, adder2_a2_p, adder2_a3_p]
    adder2_a_n = [adder2_a0_n, adder2_a1_n, adder2_a2_n, adder2_a3_n]

    # Second Adder
    adder2_s_p, adder2_s_n, adder2_c_p, adder2_c_n = adder_4bit(adder2_a_p, adder2_a_n, adder2_b_p, adder2_b_n, zero_p2, zero_n2)

    z_p[2], z_n[2] = adder2_s_p[0], adder2_s_n[0]

    adder3_b_p = [adder2_s_p[1], adder2_s_p[2], adder2_s_p[3], adder2_c_p]
    adder3_b_n = [adder2_s_n[1], adder2_s_n[2], adder2_s_n[3], adder2_c_n]

    # Third layer of ANDs
    adder3_a0_p, adder3_a0_n = and_xsfq(x_p[3][0], x_n[3][0], y_p[0][3], y_n[0][3])
    adder3_a1_p, adder3_a1_n = and_xsfq(x_p[3][1], x_n[3][1], y_p[1][3], y_n[1][3])
    adder3_a2_p, adder3_a2_n = and_xsfq(x_p[3][2], x_n[3][2], y_p[2][3], y_n[2][3])
    adder3_a3_p, adder3_a3_n = and_xsfq(x_p[3][3], x_n[3][3], y_p[3][3], y_n[3][3])

    adder3_a_p = [adder3_a0_p, adder3_a1_p, adder3_a2_p, adder3_a3_p]
    adder3_a_n = [adder3_a0_n, adder3_a1_n, adder3_a2_n, adder3_a3_n]

    # Third Adder
    adder3_s_p, adder3_s_n, adder3_c_p, adder3_c_n = adder_4bit(adder3_a_p, adder3_a_n, adder3_b_p, adder3_b_n, zero_p3, zero_n3)

    z_p[3], z_n[3] = adder3_s_p[0], adder3_s_n[0]
    z_p[4], z_n[4] = adder3_s_p[1], adder3_s_n[1]
    z_p[5], z_n[5] = adder3_s_p[2], adder3_s_n[2]
    z_p[6], z_n[6] = adder3_s_p[3], adder3_s_n[3]
    z_p[7], z_n[7] = adder3_c_p, adder3_c_n

    return z_p, z_n


def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def test_single_input(a3, a2, a1, a0, b3, b2, b1, b0):
    # Input order is MSB to LSB
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

    # Return a zero input
    zero_p_t = inv(0)
    zero_n_t = 0
    zero_p = pylse.inp_at(zero_p_t*T, name='zero_p')
    zero_n = pylse.inp_at(zero_n_t*T, name='zero_n')

    return a_p, a_n, b_p, b_n, zero_p, zero_n

def check_events(events, T):
    print(int(events['z7_p'][0] < T), int(events['z6_p'][0] < T), int(events['z5_p'][0] < T), int(events['z4_p'][0] < T), int(events['z3_p'][0] < T), int(events['z2_p'][0] < T), int(events['z1_p'][0] < T), int(events['z0_p'][0] < T))

if __name__ == "__main__":

    T = 400 # duration of a phase

    input_a = [1, 0, 1, 1]
    input_b = [1, 0, 1, 1]
    # Note: Arrays above are MSB->LSB

    # Test input
    a_p, a_n, b_p, b_n, zero_p, zero_n = test_single_input(input_a[0], input_a[1], input_a[2], input_a[3], input_b[0], input_b[1], input_b[2], input_b[3])

    # Instantiate the multiplier
    z_p, z_n = mult_4bit(a_p, a_n, b_p, b_n, zero_p, zero_n)

    z0_p, z1_p, z2_p, z3_p, z4_p, z5_p, z6_p, z7_p = z_p
    z0_n, z1_n, z2_n, z3_n, z4_n, z5_n, z6_n, z7_n = z_n

    # Probe outputs
    pylse.inspect(z0_p, 'z0_p')
    pylse.inspect(z0_n, 'z0_n')
    pylse.inspect(z1_p, 'z1_p')
    pylse.inspect(z1_n, 'z1_n')
    pylse.inspect(z2_p, 'z2_p')
    pylse.inspect(z2_n, 'z2_n')
    pylse.inspect(z3_p, 'z3_p')
    pylse.inspect(z3_n, 'z3_n')
    pylse.inspect(z4_p, 'z4_p')
    pylse.inspect(z4_n, 'z4_n')
    pylse.inspect(z5_p, 'z5_p')
    pylse.inspect(z5_n, 'z5_n')
    pylse.inspect(z6_p, 'z6_p')
    pylse.inspect(z6_n, 'z6_n')
    pylse.inspect(z7_p, 'z7_p')
    pylse.inspect(z7_n, 'z7_n')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Print out inputs
    print("Input A: " + str(input_a))
    print("Input B: " + str(input_b))
    print("A x B = ", end="")

    # Print out the events
    check_events(events, T)