from collections import namedtuple
import pylse


###############
# DRO2R       #
###############
class DRO2R(pylse.SFQ):
    ''' Destructive read-out (AKA DFF) element with 2 read out port

    Numbers follows that in DRO temporarily.
    '''
    _setup_time = 2.0
    _hold_time = 2.0

    name = 'DRO2R'
    inputs = ['a', 'clk0','clk1']
    outputs = ['q0','q1']
    transitions = [
        {'id': '0', 'source': 'idle',      'trigger': 'a',   'dest': 'a_arrived','priority': 1},
        {'id': '1', 'source': 'idle',      'trigger': ['clk0','clk1'], 'dest': 'idle',
         'transition_time': _hold_time,    'past_constraints': {'*': _setup_time},'priority': 0},
        {'id': '2', 'source': 'a_arrived', 'trigger': 'a',   'dest': 'a_arrived','priority': 1},
        {'id': '3', 'source': 'a_arrived', 'trigger': 'clk0', 'dest': 'idle',
         'transition_time': _hold_time,    'past_constraints': {'*': _setup_time},
         'firing': 'q0','priority': 0},
        {'id': '4', 'source': 'a_arrived', 'trigger': 'clk1', 'dest': 'idle',
         'transition_time': _hold_time,    'past_constraints': {'*': _setup_time},
         'firing': 'q1','priority': 0},
    ]
    jjs = 6
    firing_delay = 5.8


###############
# Flip Flops  #
###############
class DRO(pylse.SFQ):
    ''' Destructive read-out (AKA DFF) element

    added here to allow for easy modification.
    '''
    _setup_time = 2.0
    _hold_time = 2.0

    name = 'DRO'
    inputs = ['a', 'clk']
    outputs = ['q']
    transitions = [
        {'id': '0', 'source': 'idle',      'trigger': 'a',   'dest': 'a_arrived'},
        {'id': '1', 'source': 'idle',      'trigger': 'clk', 'dest': 'idle',
         'transition_time': _hold_time,    'past_constraints': {'*': _setup_time}},
        {'id': '2', 'source': 'a_arrived', 'trigger': 'a',   'dest': 'a_arrived'},
        {'id': '3', 'source': 'a_arrived', 'trigger': 'clk', 'dest': 'idle',
         'transition_time': _hold_time,    'past_constraints': {'*': _setup_time},
         'firing': 'q'},
    ]
    jjs = 4
    firing_delay = 7.0


################
# Asynchronous #
################
class PTL(pylse.SFQ):
    ''' Passive Transmission Line

    A wire routing pulses from input to output and Firing Delay come from [1] (page 9 prose)
    '''
    name = 'PTL'
    inputs = ['a']
    outputs = ['q']
    transitions = [
        {'source': 'idle', 'trigger': 'a', 'dest': 'idle', 'firing': 'q'},
    ]
    jjs = 0
    firing_delay = 378.3


class M(pylse.SFQ):
    ''' Merger Element

    Default numbers for JJs and Firing Delay come from [2].
    Transition time comes from the fact that if you receive an input while firing,
    you'd normally want that to be an error since that input pulse is usually phyiscally
    swallowed up.
    '''
    name = 'M'
    inputs = ['a', 'b']
    outputs = ['q']
    firing_delay = 8.2
    transitions = [
        {'source': 'idle', 'trigger': 'a', 'firing': 'q', 'dest': 'idle',
         'transition_time': firing_delay},
        {'source': 'idle', 'trigger': 'b', 'firing': 'q', 'dest': 'idle',
         'transition_time': firing_delay},
    ]
    jjs = 7


class S(pylse.SFQ):
    ''' Splitter Element

    Default numbers for JJs and Firing Delay come from [1].
    These also agree with the numbers from [2].
    '''
    name = 'S'
    inputs = ['a']
    outputs = ['l', 'r']
    firing_delay = 0
    transitions = [
        {'source': 'idle', 'trigger': 'a', 'dest': 'idle', 'firing': ['l', 'r'],
         'transition_time': firing_delay},
    ]
    jjs = 3



def dro2r(in0: pylse.Wire, clk0: pylse.Wire, clk1:pylse.Wire, left_name=None, right_name=None, **overrides):
    ''' Create and connect a DRO2R

    :param Wire in0: input wire
    :param Wire clk0: input wire
    :param Wire clk1: input wire traditionally corresponding to a clock signal
    :param str name: Name to give the output wire
    :param dict overrides: keyword arguments for overriding defaults of the element,
        such as: jjs, firing_delay, transition_time, error_transitions.
    :return: output wire from the DRO element
    '''
    DRO2R_out = namedtuple('DRO2R_out',['out0','out1'])
    out0,out1 = pylse.Wire(left_name), pylse.Wire(right_name)
    pylse.working_circuit().add_node(DRO2R(**overrides), [in0, clk0, clk1], [out0,out1])
    return DRO2R_out(out0=out0,out1=out1)

def dro(in0: pylse.Wire, clk: pylse.Wire, name=None, **overrides):
    ''' Create and connect a DRO

    :param Wire in0: input wire
    :param Wire clk: input wire traditionally corresponding to a clock signal
    :param str name: Name to give the output wire
    :param dict overrides: keyword arguments for overriding defaults of the element,
        such as: jjs, firing_delay, transition_time, error_transitions.
    :return: output wire from the DRO element
    '''
    out = pylse.Wire(name)
    pylse.working_circuit().add_node(DRO(**overrides), [in0, clk], [out])
    return out



def ptl(in0: pylse.Wire, out0: pylse.Wire, name=None, **overrides):
    ''' Create and connect a PTL

    :param Wire in0: input wire
    :param str name: Name to give the output wire
    :param dict overrides: keyword arguments for overriding defaults of the element,
        such as: jjs, firing_delay, transition_time, error_transitions.
    '''
    # out = pylse.Wire(name) 
    # here you are creating a new Wire so the output and the original wire did not connect
    pylse.working_circuit().add_node(PTL(**overrides), [in0], [out0])
    return

def m(in0: pylse.Wire, in1: pylse.Wire, name=None, **overrides):
    ''' Create and connect an M element

    :param Wire in0: first input
    :param Wire in1: second input
    :param str name: Name to give the output wire
    :param dict overrides: keyword arguments for overriding defaults of the element,
        such as: jjs, firing_delay, transition_time, error_transitions.
    '''
    out = pylse.Wire(name)
    pylse.working_circuit().add_node(M(**overrides), [in0, in1], [out])
    return out


def s(in0: pylse.Wire, left_name=None, right_name=None, **overrides):
    ''' Create and connect a single splitter element

    :param Wire in0: wire to split
    :param str left_name: Name to give the left output wire
    :param str right_name: Name to give the right output wire
    :param dict overrides: keyword arguments for overriding defaults of the element,
        such as: jjs, firing_delay, transition_time, error_transitions.
    :return namedtuple: a tuple for accessing the outputs, .left and .right
    '''
    S_out = namedtuple('S_out', ['out1', 'out2'])
    out1, out2 = pylse.Wire(left_name), pylse.Wire(right_name)
    pylse.working_circuit().add_node(S(**overrides), [in0], [out1, out2])
    return S_out(out1=out1, out2=out2)