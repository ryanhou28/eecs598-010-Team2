import pylse


# Define xSFQ Cells needed
def dro_c(*args):
    return pylse.dro_c(*args, firing_delay=5.1)

def dro(*args):
    return pylse.dro(*args, firing_delay=5.1)

def dro_sr(*args):
    return pylse.dro_sr(*args, firing_delay=5.1)

def s(x):
    return pylse.s(x, firing_delay=4.3)

def m(*args):
    return pylse.m(*args, firing_delay=8.2)

def jtl(in0: pylse.Wire, out0: pylse.Wire, name=None, **overrides):
    pylse.working_circuit().add_node(pylse.sfq_cells.JTL(**overrides), [in0], [out0])
    return


def alt_clock(clk):
    """"
    Alternating phase clock generator
    clk: input clock signal
    """

    # Instantiate an input wire to the DRO_C
    dro_in = pylse.Wire()

    clk_o, clk_e = dro_c(dro_in, clk)

    clk_e_spl = pylse.split(clk_e, 2)

    jtl(clk_e_spl[1], dro_in)

    return clk_o, clk_e_spl[0]


def sr_to_dr(a, clk_o, clk_e):
    """
    Convert from single rail to dual rail
    """
    
    # Split clock
    clk_o0, clk_o1 = s(clk_o)

    # First DRO_C
    dro_c_p, dro_c_n = dro_c(a, clk_e)

    # Split DRO_C outputs
    dro_c_p0, dro_c_p1 = s(dro_c_p)
    dro_c_n0, dro_c_n1 = s(dro_c_n)

    # Top DRO
    dro_1 = dro(dro_c_p0, clk_o0)
    
    # Bottom DRO
    dro_2 = dro(dro_c_n0, clk_o1)

    # First Merger
    a_p = m(dro_c_p1, dro_2)

    # Second Merger
    a_n = m(dro_1, dro_c_n1)

    return a_p, a_n
    

def dr_to_sr(a_p, a_n, clk):
    """
    Convert from dual rail to single rail
    """
    
    return dro_sr(a_n, a_p, clk)

# TEST FUNCTIONS


def test_alt_clock():
    T = 150
    clk = pylse.inp(start=T/2, period=T, n=8, name='clk')

    clk_o, clk_e = alt_clock(clk)

    # Probe outputs
    pylse.inspect(clk, 'clk')
    pylse.inspect(clk_o, 'clk_o')
    pylse.inspect(clk_e, 'clk_e')

    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
    sim.print_state()

def test_sr_to_dr():
    T = 50
    starting_delay = 20
    clk_e = pylse.inp(start=starting_delay, period=T, n=8, name='clk_e')
    clk_o = pylse.inp(start=starting_delay+T/2, period=T, n=8, name='clk_o')

    a = pylse.inp_at(100, name='a')

    a_p, a_n = sr_to_dr(a, clk_o, clk_e)

    # Probe outputs
    pylse.inspect(clk_e, 'clk_e')
    pylse.inspect(clk_o, 'clk_o')
    pylse.inspect(a, 'a')
    pylse.inspect(a_p, 'a_p')
    pylse.inspect(a_n, 'a_n')

    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
    sim.print_state()

def test_dr_to_sr():
    T = 50

    clk = pylse.inp(start=T/2, period=T, n=8, name='clk')

    a_p = pylse.inp_at(10, 40, name='a_p')
    a_n = pylse.inp_at(15, 35, name='a_n')

    a = dr_to_sr(a_p, a_n, clk)

    # Probe outputs
    pylse.inspect(clk, 'clk')
    pylse.inspect(a_p, 'a_p')
    pylse.inspect(a_n, 'a_n')
    pylse.inspect(a, 'a')

    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()
    sim.print_state()

if __name__ == "__main__":
    test_alt_clock()
    # test_sr_to_dr()
    # test_dr_to_sr()
