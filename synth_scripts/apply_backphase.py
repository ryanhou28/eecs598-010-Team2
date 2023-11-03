from backphase import survivor_phases, backtrack_bitvector
from typing import Dict
from readaig import Aag
import numpy as np
import numpy.typing as npt
from enum import Enum

npbo = npt.NDArray[np.bool_]


class Nettype(Enum):
    AND = 1
    OR = 2
    PAIR = 3


def final_phase(
        phases: npbo) -> npbo:
    """
    Find the phase asignment that satisfies all nodes that are not duplicated
    """
    final = np.any(phases, axis=0)
    ll = len(final)//2
    negfin = final[ll:]
    final = np.concatenate([np.logical_not(negfin), negfin])
    return final


def aag_to_nettype(aag: Aag) -> tuple[Dict[int, Nettype], npt.NDArray]:
    """
    Assign a gate type to each node at found
    polarity assignment.
    No conflict with output assignment -> AND
    No conflict after demorgan -> OR
    Conflict either way -> PAIR
    """
    n_out = aag.out_cnt
    phases = backtrack_bitvector(aag)
    unduped = survivor_phases(phases)
    if (len(unduped) > 0):
        unphased = np.vstack(list(unduped.values()))
        final = final_phase(unphased)
    else:
        final = np.concatenate(
            [np.zeros(n_out, dtype=bool), np.ones(n_out, dtype=bool)])
    return {i: phase_comp(nstate.phases, final)
            for i, nstate in phases.items()}, final


def phase_comp(phase: npbo, final: npbo) -> Nettype:
    """ Type of gate implied by node's phase compatibility with assignment """
    n = len(final)//2
    dm_final = np.concatenate((final[n:], final[:n]))
    # Get conflicts
    dm_conflict = np.any(np.bitwise_and(phase, final))
    conflict = np.any(np.bitwise_and(phase, dm_final))
    # Cast to enum index
    con = 2*conflict + dm_conflict
    con = np.maximum(con, 1)
    return Nettype(int(con))
