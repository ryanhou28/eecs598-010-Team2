import numpy as np
import numpy.typing as npt
from typing import Dict, List, TypeAlias
from dataclasses import dataclass
from itertools import groupby
from readaig import Aag
bitvec = npt.NDArray[np.bool_]


@dataclass
class nodestate:
    seen: bitvec
    phases: bitvec


# Big assumpion: the aag has nodes in topological order
def backtrack_bitvector(aag: Aag) -> Dict[int, nodestate]:
    """
    Given an Aag struct get the phase relations of each
    node with the outputs.
    Nodes are assumed to be in topological order.
    """
    phase_assign = init_pols(aag)
    # Iterate through the nodes in reverse topological order
    for node in reversed(sorted(aag.nodes.keys())):
        # Iterate through ingoing edges and update
        ((in1, pol1), (in2, pol2)) = aag.nodes[node]
        if (in1 > aag.in_cnt):
            phase_assign[in1] = update_nodestate(
                phase_assign[node].phases, bool(pol1), phase_assign[in1])
        if (in2 > aag.in_cnt):
            phase_assign[in2] = update_nodestate(
                phase_assign[node].phases, bool(pol2), phase_assign[in2])
    return phase_assign


# Get candidate nodes and their phases
def get_forceds(nstates: Dict[int, nodestate]
                ) -> List[int]:
    """Nodes that belong to a loop with odd inverters thus have
    to be duplicated in every phase assignment"""
    multis = {k: v for k, v in nstates.items() if len(v.seen) > 1}
    # Remove forced duplicates
    forceds = [k for k, v in multis.items() if isforced(v.phases)]
    return forceds


def get_candidates(nstates: Dict[int, nodestate]
                   ) -> Dict[int, bitvec]:
    """Get candidate nodes, the non-reconvergent multifanout nodes
    that determine output assignment and their phases"""
    # Maybe filter multifanouts first
    multis = {k: v for k, v in nstates.items() if len(v.seen) > 1}
    # Check for disjoints that are not forced
    cands = {k: v.phases for k, v in multis.items()
             if is_disjoint(v.seen) and not isforced(v.phases)}
    # Return (forceds?) and candidates
    return cands


def is_disjoint(samples: bitvec) -> bool:
    return not np.all(samples @ samples.T)


def isforced(phass: bitvec) -> bool:
    lt = len(phass)//2
    pos = phass[:lt]
    neg = phass[lt:]
    odd_loop = np.any(np.logical_and(pos, neg))
    return bool(odd_loop)


def init_pols(aag: Aag) -> Dict[int, nodestate]:
    pol_needs = {}
    width = aag.out_cnt
    for nod in aag.nodes.keys():
        pol_needs[nod] = nodestate(
            seen=np.empty((0, width), dtype=bool),
            phases=np.zeros(width*2, dtype=bool))
    # for nod, (out_ind, pol) in aag.out_lut.items():
    for out_ind, (nod, pol) in enumerate(aag.out_lut):
        # This takes into account initial output polarity, unsure if useful
        if (nod > aag.in_cnt):
            set_ind = (pol*aag.out_cnt) + out_ind
            pol_needs[nod].phases[set_ind] = True
            onehot = np.zeros((1, width), dtype=bool)
            onehot[0, out_ind] = True
            pol_needs[nod].seen = onehot
    return pol_needs


def update_nodestate(
        target_bv: bitvec, pol: bool, self_bv: nodestate) -> nodestate:
    """Update list of seen phases and own phase assignment
    from a fanout node"""
    lt = len(target_bv)//2
    if pol:
        target_bv = np.concatenate((target_bv[lt:], target_bv[:lt]))
    new_fo = np.logical_or(target_bv[lt:], target_bv[:lt])
    new_seen = np.vstack((self_bv.seen, new_fo))
    new_phases = np.logical_or(self_bv.phases, target_bv)
    new_nstate = nodestate(new_seen, new_phases)
    return new_nstate


def find_multifanouts(aag: Aag) -> List[int]:
    "List of nodes with more than one fanout"
    valz = aag.nodes.values()
    ar = []
    for (a, _), (b, _) in valz:
        ar.extend([a, b])
    multifos = map(lambda x: x[0],
                   filter(lambda x: len(x) > 1,
                   groupby(sorted(ar))))
    return list(multifos)


# Matrix representation of graph
adj_mat: TypeAlias = npt.NDArray[np.bool_]


def incompat_graph(cands: Dict[int, bitvec]) -> adj_mat:
    """Build incompatibility graph between candidate nodes
    Remember inverted phases check"""
    # Make matrix from candidate phase assignments
    cand_mat = np.vstack(list(cands.values()))
    width = np.atleast_2d(cand_mat).shape[1]
    n_out = width//2
    posa = cand_mat[:, :n_out]
    nega = cand_mat[:, n_out:]
    # Check which are incompatible(in both polarities)
    pncompat = posa @ nega.T
    ppcompat = posa @ posa.T
    compat = np.logical_and(ppcompat, pncompat)
    return compat


def incompat_posneg(cands: Dict[int, bitvec]) -> adj_mat:
    """Build incompatibility graph between candidate nodes
    Nodes for both normal and inverted phases per gate"""
    # Make matrix from candidate phase assignments
    cand_mat = np.vstack(list(cands.values()))
    width = np.atleast_2d(cand_mat).shape[1]
    n_out = width//2
    posa = cand_mat[:, :n_out]
    nega = cand_mat[:, n_out:]
    # Check which are incompatible(in both polarities)
    # Nodes have same flip
    crosses = cand_mat @ cand_mat.T
    # Pos of x conflicts with Neg of y
    pncompat = posa @ nega.T
    # Nodes have different flip = p^n or n^p conflict
    dots = pncompat + pncompat.T
    dual_repr = np.block([[dots, crosses], [crosses, dots]])
    return dual_repr


def heuristic_selection(admat: adj_mat) -> List[int]:
    """Heuristic solution from the paper, just remove
    highest degree node iteratively until no connections
    Returns removed indexes, not node codes"""
    am = np.copy(admat)
    duped_cands = []
    while np.any(am):
        max_idx = np.argmax(np.sum(am, axis=0))
        duped_cands.append(max_idx)
        am[max_idx, :] = 0
        am[:, max_idx] = 0
    return duped_cands


def survivor_phases(phases: Dict[int, nodestate]) -> Dict[int, bitvec]:
    """Run all procedures to get nodes that need duplication,
    then return the phase constraints, inverted if the demorgan of the node
    is selected, of those that are not duplicated and their phases.
    Dual representation (normal and demorgan) of phase constraints is used.
    """
    cands = get_candidates(phases)
    if (len(cands) == 0):
        return {}
    ic_graph = incompat_posneg(cands)
    extradup = heuristic_selection(ic_graph)
    # Translate index
    return translate_index(cands, extradup)


def translate_index(cands: Dict[int, bitvec], extradup: List[int]
                    ) -> Dict[int, bitvec]:
    n_cand = len(cands)
    survived = [(list(cands.keys())[i % n_cand], i // n_cand != 0)
                for i in range(2*len(cands)) if i not in extradup]
    survivor_phases = {i: cond_flip(cands[i], flip)
                       for i, flip in survived}
    return survivor_phases


def cond_flip(x, b):
    n = len(x)//2
    return np.concatenate((x[n:], x[:n])) if b else x
