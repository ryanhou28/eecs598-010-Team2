from readaig import merge_outs
import aiger as ag
from aiger import AIG
from backphase import Aag
import numpy as np
import numpy.typing as npt


def aagdup(aag: Aag, phase: list[bool]) -> AIG:
    nods = {}
    ouch = {}
    nods[0] = ag.atom(False)
    nods[1] = ag.atom(True)
    for i in range(aag.in_cnt):
        ni = i + 1
        nods[2 * ni] = ag.atom(f'i{ni}_0')
        nods[2 * ni + 1] = ag.atom(f'i{ni}_1')
    for gate, ((in1, p1), (in2, p2)) in aag.nodes.items():
        pa, na = 2 * in1, 2 * in1 + 1
        pa, na = (pa, na) if p1 == 0 else (na, pa)
        pb, nb = 2 * in2, 2 * in2 + 1
        pb, nb = (pb, nb) if p2 == 0 else (nb, pb)
        pga, nga = 2 * gate, 2 * gate + 1
        nods[pga] = nods[pa] & nods[pb]
        nods[nga] = nods[na] | nods[nb]
    # for po, (out_ind, out_pol) in aag.out_lut.items():
    for out_ind, (po, out_pol) in enumerate(aag.out_lut):
        pol = out_pol ^ phase[out_ind]
        ouch[out_ind] = nods[2 * po + pol]
    return merge_outs(ouch)
