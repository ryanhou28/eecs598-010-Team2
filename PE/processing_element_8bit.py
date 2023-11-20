"""
processing_element_8bit.py

The 8bit processing element is the building block of the systolic array
"""

import pylse
import shift_register, simple_memory, feedback_mem_w_external_write
import sys

sys.path.append('../')
from MAC.Adder.adder_8bit_syn_structural_N_PyLSE import adder, twos_to_dec, twos_complement_bin
from MAC.Mult.mult_comb_syn_structural_N_PyLSE import mult

def processing_element_8bit_internal_weight(input_feature, valid_in, weight_in, weight_write, clk):
    """
    An 8bit feature processing element.

    This design uses a shift-register memory with feedback to hold the weights.
    We may want to consider using an external DLM to storm these weights.

    parameters:
        input_feature
            8 wires for the input feature
        valid_in
            1 wire do denote that it is the last input
            TODO this may be a bad choice of name
        weight_in
            8 wires to cary the weights into the weight memory
        weight_write
            wire to denote that a weight is being written
        clk
            the clk signal
    
    """

    # How many cycles is the PE?
    N_CYCLES = 5 # TODO this is a made up number
    N_BITS = len(input_feature)

    # TODO split clk for all the elements that need it.

    ##########################################################################
    # input feature
    ##########################################################################

    # Split the input_feature to 2 for:
    # 0 -> the multiplier
    # 1 -> the input_feature shift register
    input_feature_split = [[], []]
    for i in range(N_BITS):
        f_a, f_b = pylse.split(input_feature[i])
        input_feature_split[0].append(f_a)
        input_feature_split[1].append(f_b)

    # The input feature shift register memory 
    # TODO this can be simplified to use fewer DROs by being a bit more clever
    input_feature_out = shift_register.sr_N_bit(input_feature_split[1], clk, N_CYCLES, N_BITS)

    ##########################################################################
    # Weights Memory
    ##########################################################################

    # A couple of notes on an internal weight memory
    # We need to write from an external source on command
    # We only want to shift when we have a new input_feature or we are writing a new memory and not every cycle
    # That means we will probably need a new input for current_input_feature_valid or something like that.

    # TODO modify feedback_mem_w_external_write to work in this case

    ##########################################################################
    # The Multiplier
    ##########################################################################

    # TODO the multiplier
    mult_out = [pylse.Wire() for i in range(N_BITS)]

    ##########################################################################
    # Valid Shift Register
    ##########################################################################

    valid_sr_out = shift_register.sr_single_bit(valid_in, clk, N_CYCLES)
    # Split the output from the valid_sr_out to 3 for:
    # 0 -> The valid_in for the next PE
    # 1 -> The reset for the accumulator memory
    # 2 -> The valid signal for the feature output 
    valid_out_split = pylse.split(valid_sr_out, 3)

    ##########################################################################
    # The Accumulator Memory
    ##########################################################################

    accumulator_in = [pylse.Wire() for i in range(N_BITS)] # TODO change the name of this variable
    accumulator_in = simple_memory.simple_mem_N_bit(accumulator_out_split[0], valid_out_split[1], clk, N_BITS)
    
    ##########################################################################
    # The Accumulator Itself
    ##########################################################################

    # mult_out from the multiplier
    # accumulator_in from memory
    accumulator_out = adder_8bit_syn_structural_N_PyLSE.mymod()

    # split the accumulator_out into 2 for:
    # 0 -> the accumulator memory
    # 1 -> the AND block
    accumulator_out_split = [[], []]
    for i in range(N_BITS):
        f_a, f_b = pylse.split(accumulator_out[i])
        accumulator_out_split[0].append(f_a)
        accumulator_out_split[1].append(f_b)

    ##########################################################################
    # The AND Block
    ##########################################################################
    
    # TODO the AND block
    # I don't know the best way of doing this?
    and_out = [pylse.Wire() for i in range(N_BITS)]
    and_valid_split = pylse.split(valid_out_split[2], N_BITS)

    # Using ANDs will add another clock cycle
    for i in range(N_BITS):
        and_out[i] = pylse.and_s(accumulator_out_split[1][i], and_valid_split[i], clk)
    

    return and_out, input_feature_out, valid_out_split[0]



def processing_element_8bit_external_weight(input_feature, valid_in, weight_in, clk):
    """
    An 8bit feature processing element with external weights.

    parameters:
        input_feature
            8 wires for the input feature
        valid_in
            1 wire do denote that it is the last input
            TODO this may be a bad choice of name
        weight_in
            8 wires to cary the weights for the current multiply
        clk
            the clk signal
    
    """

    # This should be very similar to what I have put together for the internal weight version

    raise NotImplementedError

