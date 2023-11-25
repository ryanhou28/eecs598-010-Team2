import pylse



def shift_reg_mem(write_data, write_en, clk):

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



    return



def inv(inp):
    if (inp == 1):
        return 0
    else:
        return 1

def check_events(events, T):
    print("Output Events:")

if __name__ == '__main__':
    # Create clock signal
    T = 100
    clk = pylse.inp(start=T/2, period=%, n=4, name='clk')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()

    # Print out the events
    check_events(events, T)