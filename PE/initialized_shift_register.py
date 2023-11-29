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

class DRO_C_init_1(pylse.SFQ):
    ''' Destructive read-out element with complementary outputs (AKA DFF with compl. outputs)

    Currently just using similar numbers from DRO.
    '''
    _setup_time = 1.2
    _hold_time = 0.0

    name = 'DRO_C'
    inputs = ['a', 'clk']
    outputs = ['q', 'qnot']
    transitions = [
        {'id': '0', 'source': 'low',  'trigger': 'a',   'dest': 'idle'},
        {'id': '1', 'source': 'low',  'trigger': 'clk', 'dest': 'low',   'transition_time': _hold_time, 'past_constraints': {'*': _setup_time},  'firing': 'qnot'},
        {'id': '2', 'source': 'idle', 'trigger': 'a',   'dest': 'idle'},
        {'id': '3', 'source': 'idle', 'trigger': 'clk', 'dest': 'low',   'transition_time': _hold_time,  'past_constraints': {'*': _setup_time}, 'firing': 'q'},
    ]
    jjs = 13
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

def dro_c_init_1(a: pylse.Wire, clk: pylse.Wire):
    out = pylse.Wire()
    pylse.working_circuit().add_node(DRO_C_init_1(), [a, clk], [out])
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

def dro_c(*args):
    """
    Destructive readout with complimentry readout
    """
    return pylse.dro_c(*args, firing_delay=5.1)

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

    Shift register array is n_bits deep, length wide
    Output is n_bits wide
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

    Shift register array is same dimensions as init_states
    Output has same width as init_states
    """

    length = len(init_states)
    n_bits = len(init_states[0])

    # Transpose the array
    init_states = [list(row) for row in zip(*init_states)]
    

    return sr_N_bit_initialized(x, clk, length, n_bits, init_states)
    
def create_sr_from_int_list(x, clk, int_list):
    """
    Creates a shift register with 8 bit ints based on a list of ints
    Note: Uses two's complement.
    
    """

    def twos_comp(val, bits=8):
        """compute the 2's complement of int value """
        if bits == 0:      # Use as many bits needed for the value.
            bits = val.bit_length()
        return f"{str(bin(((val & (2 ** bits) - 1) - (2 ** bits)) * -1))[2:]:08}"
    
    init_states = [[] for i in range(8)]

    for a_int in int_list:
        tc = twos_comp(a_int)
        for i in range(8):
            init_states[i].append(int(tc[i]))

    return create_sr_from_init_states(x, clk, init_states)
        

#####################################################
# Shift Registers with loopback and final dro_c layer
#####################################################

def sr_single_bit_recursive_initialized_dro_c(x, clk, length, init_state):
    """
    A parametric shift register. Many dro's in series

    TODO find a better way than recursive
    """

    state = init_state[-1]

    if length == 1:
        if state == 1:
            return dro_c_init_1(pylse.jtl(x), clk[0])
        else:
            return dro_c(pylse.jtl(x), clk[0])
    else:
        if state == 1:
            return dro_init_1(pylse.jtl(sr_single_bit_recursive_initialized(x,clk,length-1, init_state[:-1])), clk[length-1])
        else:
            return dro(pylse.jtl(sr_single_bit_recursive_initialized(x,clk,length-1, init_state[:-1])), clk[length-1])

def sr_single_bit_initialized_loopback__dro_c(x, clk, length, init_state):
    """
    A parametric shift register. Many dro's in series

    TODO find a better way than recursive
    """

    raise NotImlementedError

    clk_fo = pylse.split(clk, length)

    lb_wire = pylse.Wire()

    return sr_single_bit_recursive_initialized(x, clk_fo, length, init_state)

if __name__ == "__main__":

    T = 80  # duration of a phase
    clk = pylse.inp(start=T/2, period=T, n=10, name='clk')

    x_in_arr = []
    for i in range(8):
        x_in_arr.append(pylse.inp_at(5*T))
    
    x_out_arr = create_sr_from_int_list(x_in_arr, clk, [1,127])

    # Probe outputs
    pylse.inspect(clk, 'clk')
    for i in range(8):
        pylse.inspect(x_in_arr[i], f'x_in_{i}')
        pylse.inspect(x_out_arr[i], f'x_out_{i}')

    # Run simulation
    sim = pylse.Simulation()
    events = sim.simulate()
    sim.plot()