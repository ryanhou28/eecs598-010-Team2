import backphase
import os
from typing import List
import numpy as np
import numpy.typing as npt
from apply_backphase import final_phase, phase_comp, aag_to_nettype
from readaig import Aag, read_Aag_struc, simboth, sample_bits
from aigdup import aagdup

papers_phases = [
    [2, 2, 0, 2, 0],
    [1, 0, 2, 0, 0],
    [2, 0, 2, 2, 0],
    [0, 0, 2, 2, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 1],
    [0, 0, 0, 2, 1],
]


loop_phases = [
    [2, 2, 0],
    [0, 2, 2],
    [1, 0, 2],
]


def quick2phase(x: list[int]) -> npt.NDArray[np.bool_]:
    xx = np.array(x)
    xp = xx // 2
    xn = xx % 2
    return np.concatenate((xp, xn)).astype(bool)


def qu2rm(phases: List[List[int]]) -> List[int]:
    phs = {i: quick2phase(x) for i, x in enumerate(phases)}
    ig = backphase.incompat_posneg(phs)
    rm = backphase.heuristic_selection(ig)
    return rm


def cond_flip(x, b):
    n = len(x) // 2
    return np.concatenate((x[n:], x[:n])) if b else x


def check_rem(phs, rm):
    n = len(phs)
    surv = [i for i in range(2 * n) if i not in rm]
    remain = np.array([cond_flip(phs[i % n], i > n) for i in surv])
    # Rip this off in main thread
    assignment = np.any(remain, axis=0)
    pos, neg = np.split(assignment, 2)
    assert not np.any(pos & neg)
    assert np.all(pos | neg)


def check_finalphase(phases):
    """Get a maping from mock phase assignment candidates"""
    hm = qu2rm(phases)
    fake_dic = {i * 10: quick2phase(phases[i]) for i in range(7)}
    surv = backphase.translate_index(fake_dic, hm)
    sv = np.vstack(list(surv.values()))
    fi = final_phase(sv)
    ph = [phase_comp(s, fi) for s in sv]
    return ph


def map_back_fa(aag_fn: str):
    j = read_Aag_struc(aag_fn)
    return aag_to_nettype(j)


def doublecount(
    phases: npt.NDArray[np.bool_], final: npt.NDArray[np.bool_]
) -> int:
    """Given phase assignments for all nodes and a (hypothetical)
    final assignment return the number of gates that would be duplicated"""
    n = len(final) // 2
    dm_final = np.concatenate((final[n:], final[:n]))
    dm_conflict = np.any(np.bitwise_and(phases, final), axis=1)
    conflict = np.any(np.bitwise_and(phases, dm_final), axis=1)
    doops = np.bitwise_and(dm_conflict, conflict)
    n_duped = np.sum(doops)
    return n_duped


def aag2phase_mat(aag: Aag) -> npt.NDArray[np.bool_]:
    phases = backphase.backtrack_bitvector(aag)
    ph_l = [v.phases for v in phases.values()]
    return np.vstack(ph_l)


def output_phase_variance(aag: Aag, n_sample: int) -> list[int]:
    phases = aag2phase_mat(aag)
    rng_finals = np.random.choice([False, True], size=(n_sample, aag.out_cnt))
    rng_finals = np.hstack((rng_finals, np.bitwise_not(rng_finals)))
    dup_cnts = [doublecount(phases, fi) for fi in rng_finals]
    return dup_cnts


def aag_to_backphase_cnt(aag: Aag) -> int:
    """Return the number of duplicated gates the heuristic's assignment gives
    for testing purposes.
    """
    n_out = aag.out_cnt
    phases = backphase.backtrack_bitvector(aag)
    unduped = backphase.survivor_phases(phases)
    if len(unduped) > 0:
        unphased = np.vstack(list(unduped.values()))
        final = final_phase(unphased)
    else:
        final = np.concatenate(
            [np.zeros(n_out, dtype=bool), np.ones(n_out, dtype=bool)]
        )
    ph_l = [v.phases for v in phases.values()]
    phs = np.vstack(ph_l)
    return doublecount(phs, final)


def bigtry(folder: str):
    varis = {}
    for fn in os.listdir(folder):
        print(fn)
        ffn = f'{folder}/{fn}'
        aag = read_Aag_struc(ffn)
        opv = output_phase_variance(aag, 100)
        varis[fn] = opv
    return varis


def heurcnt(folder: str):
    heurdup = {}
    for fn in os.listdir(folder):
        ffn = f'{folder}/{fn}'
        print(fn)
        aag = read_Aag_struc(ffn)
        hdup = aag_to_backphase_cnt(aag)
        heurdup[fn] = hdup
    return heurdup


def nodaiinct(aii):
    return int(str(aii).split('\n')[0].split(' ')[-1])


def doublecount_vs_dupedaig(aag: Aag) -> tuple[int, int]:
    'To test nodephase estimate of duped gates consistant \
with duped aig with selected outputs'
    ran = np.random.choice([False, True], size=(aag.out_cnt))
    dran = np.hstack((ran, np.bitwise_not(ran)))
    aii = aagdup(aag, ran)  # type: ignore
    phaseblk = aag2phase_mat(aag)
    dc = doublecount(phaseblk, dran)
    nc = nodaiinct(aii) - aag.node_cnt
    return dc, nc


def simul_phaseddup(saig, aag, n=1):
    ran = np.random.choice([False, True], size=(aag.out_cnt))
    xaig = aagdup(aag, ran)  # type: ignore
    results = True
    for _ in range(n):
        ss, xx = simboth(saig, xaig, sample_bits(aag.in_cnt))
        difssxx = {k: v ^ xx[k] for k, v in ss.items()}
        ok = [difssxx[f'o{i}'] == ran[i] for i in range(len(ran))]
        results = results & np.all(ok)
    return results
