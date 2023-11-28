"""
initialized_shift_register.py

Shift registers that can initialized to a given state.

"""

# imports
import pylse 

###############################
# make some custom cells
###############################

class DRO_init_1(pylse.SFQ):
    ''' Destructive read-out (AKA DFF) element

    Numbers come from [1].
    '''
    _setup_time = 2.3
    _hold_time = 0.0

    name = 'DRO'
    inputs = ['a', 'clk']
    outputs = ['q']

    # We are going to rename such that idle is the "high" state
    transitions = [
        {'id': '0', 'source': 'low', 'trigger': 'clk', 'dest': 'low',     'transition_time': _hold_time,    'past_constraints': {'*': _setup_time}},
        {'id': '1', 'source': 'low', 'trigger': 'a',   'dest': 'idle'},
        {'id': '2', 'source': 'idle',      'trigger': 'a',   'dest': 'idle'},
        {'id': '3', 'source': 'idle',      'trigger': 'clk', 'dest': 'low',     'transition_time': _hold_time,    'past_constraints': {'*': _setup_time}, 'firing': 'q'},
        
    ]
    jjs = 6
    firing_delay = 5.1

class DRO_SR_init_1(pylse.SFQ):
    ''' Destructive read-out element with set-reset inputs.

    Currently just using similar numbers from DRO.
    '''
    _setup_time = 1.2
    _hold_time = 0.0

    name = 'DRO_SR'
    inputs = ['set', 'rst', 'clk']
    outputs = ['q']
    transitions = [
        {'id': '0', 'source': 'low',  'trigger': 'clk', 'dest': 'low', 'transition_time': _hold_time,      'past_constraints': {'*': _setup_time}},
        {'id': '1', 'source': 'low',  'trigger': 'rst', 'dest': 'idle'},
        {'id': '2', 'source': 'low',  'trigger': 'set', 'dest': 'idle'},
        {'id': '3', 'source': 'idle', 'trigger': 'set', 'dest': 'idle'},
        {'id': '4', 'source': 'idle', 'trigger': 'rst', 'dest': 'low'},
        {'id': '5', 'source': 'idle', 'trigger': 'clk', 'dest': 'low', 'transition_time': _hold_time,      'past_constraints': {'*': _setup_time}, 'firing': 'q'},
    ]
    jjs = 13
    firing_delay = 5.1

###############################
# Helper functions
###############################

def dro_init_1(a: pylse.Wire, clk: pylse.Wire):
    out = pylse.Wire()
    pylse.working_circuit().add_node(DRO_init_1(), [a, clk], [out])
    return out

def dro_sr_init_1(a: pylse.Wire, rst: pylse.Wire, clk: pylse.Wire):
    out = pylse.Wire()
    pylse.working_circuit().add_node(DRO_SR_init_1(), [a, rst, clk], [out])
    return out

def dro(*args):
    """
    Destructive readout
    """
    return pylse.dro(*args, firing_delay=5.1)

###############################
# Shift Registers
###############################

def sr_single_bit_recursive_initialized(x, clk, length, init_state):
    """
    A parametric shift register. Many dro's in series

    TODO find a better way than recursive
    """

    state = init_state[-1]

    if length == 1:
        if state == 1:
            return dro_init_1(pylse.jtl(x), clk[0])
        else:
            return dro(pylse.jtl(x), clk[0])
    else:
        if state == 1:
            return dro_init_1(pylse.jtl(sr_single_bit_recursive_initialized(x,clk,length-1, init_state[:-1])), clk[length-1])
        else:
            return dro(pylse.jtl(sr_single_bit_recursive_initialized(x,clk,length-1, init_state[:-1])), clk[length-1])

def sr_single_bit_initialized(x, clk, length, init_state):
    """
    A parametric shift register. Many dro's in series

    TODO find a better way than recursive
    """

    clk_fo = pylse.split(clk, length)

    return sr_single_bit_recursive_initialized(x, clk_fo, length, init_state)
    
def sr_N_bit_initialized(x, clk, length, n_bits, init_states):
    """
    A stack of parametric shift register. Many dro's in series.
    """

    # The output
    x_out = []

    # Split the clk
    clk_split = pylse.split(clk, n_bits)

    for i in range(n_bits):
        x_out.append(sr_single_bit_initialized(x[i], clk_split[i], length, init_states[i]))

    return x_out

def create_sr_from_init_states(x, clk, init_states):
    """
    Create a N_bit shift register and initialize it based on init_states
    """

    n_bits = len(init_states)
    length = len(init_states[0])

    return sr_N_bit_initialized(x,clk, length, n_bits, init_states)
    

if __name__ == "__main__":

    T = 80  # duration of a phase
    clk = pylse.inp(start=T/2, period=T, n=10, name='clk')

    # Provided input: a=1, b=1, cin=0
    x_1 = pylse.inp_at(5*T, name='x_1')
    x_2 = pylse.inp_at(5*T, name='x_2')

    # Call sr_N_bit_initialized()
    # x_out_1, x_out_2 = sr_N_bit_initialized([x_1, x_2], clk, 4, 2, [[1,0,0,1],[0,1,1,0]])

    x_out_1, x_out_2 = create_sr_from_init_states([x_1, x_2], clk, [[1,0,0,1],[0,1,1,0]])

    # Probe outputs
    pylse.inspect(clk, 'clk')
    pylse.inspect(x_1, 'x_1')
    pylse.inspect(x_2, 'x_2')
    # pylse.inspect(rst, 'rst')
    pylse.inspect(x_out_1, 'x_out_1')
    pylse.inspect(x_out_2, 'x_out_2')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()