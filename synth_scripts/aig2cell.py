from readaig import merge_outs
import aiger as ag
from aiger import AIG
from backphase import Aag
from apply_backphase import Nettype, aag_to_nettype
import numpy as np
import numpy.typing as npt
import pyverilog
import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
from splitS import fixedgates
from readaig import read_Aag_struc


def aagdup2(aag: Aag, phase: list[bool]) -> AIG:
    nods = {}
    ouch = {}
    nods[0] = ag.atom(False)
    nods[1] = ag.atom(True)
    for i in range(aag.in_cnt):
        nods[2 * i] = ag.atom(aag.in_names[i]+"_p")
        nods[2 * i + 1] = ag.atom(aag.in_names[i]+"_n")
    for gate, ((in1, p1), (in2, p2)) in aag.nodes.items():
        pa, na = 2 * in1, 2 * in1 + 1
        pa, na = (pa, na) if p1 == 0 else (na, pa)
        pb, nb = 2 * in2, 2 * in2 + 1
        pb, nb = (pb, nb) if p2 == 0 else (nb, pb)
        pga, nga = 2 * gate, 2 * gate + 1
        nods[pga] = nods[pa] & nods[pb]
        nods[nga] = nods[na] | nods[nb]
    for out_ind, (po, out_pol) in enumerate(aag.out_lut):
        pol = out_pol ^ phase[out_ind]
        ouch[aag.out_names[out_ind]] = nods[2 * po + pol]
    return merge_outs_named(ouch)


def merge_outs_named(ouch):
    "Combines aig expressions of all outputs to one aig"
    # Outputs are assigned ids in the order of their node id
    # Works if original aig's outputs also followed that rule
    ouch = [v.with_output(k).aig
            for k, v in ouch.items()]
    x = ouch[0]
    # |ing aigs (instead of their expressions) combines the networks/outputs
    for h in ouch[1:]:
        x = x | h
    return x


def aag2cell(aag: Aag) -> vast.ModuleDef:
    nets, phase = aag_to_nettype(aag)
    j = phase[aag.out_cnt:] ^ phase[:aag.out_cnt]
    # Select neg part
    phase = phase[aag.out_cnt:]
    nods = {}
    ouch = []
    nods[0] = "1'b0"
    nods[1] = "1'b1"
    prtlst = []
    declst_i = []
    declst_o = []
    gatlist = []
    padlist = []  # bufs/invs in outs for complement
    for i in range(aag.in_cnt):
        nods[2 * (i+1)] = aag.in_names[i]+"_p"
        nods[2 * (i+1) + 1] = aag.in_names[i]+"_n"
    for x in aag.in_names:
        declst_i.append(vast.Input(x))
        prtlst.append(vast.Port(x, None, None, None))
        padlist.append(mkBuf(x))
        padlist.append(mkInv(x))
    for i, x in enumerate(aag.out_names):
        # suffix = "_n" if phase[i] else "_p"
        # prtlst.append(vast.Ioport(vast.Output(x)))
        prtlst.append(vast.Port(x, None, None, None))
        declst_o.append(vast.Output(x))
    ports = vast.Portlist(prtlst)
    dec_o = vast.Decl(declst_o)
    dec_i = vast.Decl(declst_i)
    for gate, ((in1, p1), (in2, p2)) in aag.nodes.items():
        pa, na = 2 * in1, 2 * in1 + 1
        pa, na = (pa, na) if p1 == 0 else (na, pa)
        pb, nb = 2 * in2, 2 * in2 + 1
        pb, nb = (pb, nb) if p2 == 0 else (nb, pb)
        pga, nga = 2 * gate, 2 * gate + 1
        nods[pga] = f"g{gate}_p"
        nods[nga] = f"g{gate}_n"
        match nets[gate]:
            case Nettype.AND:
                gatlist.append(mkAnd(nods[pa], nods[pb], nods[pga]))
            case Nettype.OR:
                gatlist.append(mkOr(nods[na], nods[nb], nods[nga]))
            case Nettype.PAIR:
                gatlist.append(mkAnd(nods[pa], nods[pb], nods[pga]))
                gatlist.append(mkOr(nods[na], nods[nb], nods[nga]))
    for out_ind, (po, out_pol) in enumerate(aag.out_lut):
        pol = (out_pol ^ phase[out_ind])
        gatype = mkInv if phase[out_ind] else mkBuf
        oname = aag.out_names[out_ind]
        lastout = gatype(nods[2 * po + pol], oname)
        ouch.append(lastout)
    wirelist = [vast.Wire(x) for x in nods.values()]
    wirelist = wirelist[2:]
    instlist = gatlist+ouch
    spl_wires, spliters = fixedgates(instlist)
    mod = vast.ModuleDef("mymod", None, ports, [dec_i, dec_o]
                         + wirelist + spl_wires + padlist + spliters)
    return mod


def mkInv(net, nout=None):
    if (nout is None):
        nout = net + "_n"
    inp = vast.PortArg(None, vast.Identifier(net))
    outp = vast.PortArg(None, vast.Identifier(nout))
    ary = vast.Instance("not", "", (outp, inp), tuple([]))
    ark = vast.InstanceList("not", tuple([]), tuple([ary]))
    return ark


def mkBuf(net, nout=None):
    if (nout is None):
        nout = net + "_p"
    inp = vast.PortArg(None, vast.Identifier(net))
    outp = vast.PortArg(None, vast.Identifier(nout))
    ary = vast.Instance("buf", "", (outp, inp), tuple([]))
    ark = vast.InstanceList("buf", tuple([]), tuple([ary]))
    return ark


def mkOr(in1, in2, out):
    pr0 = vast.PortArg(None, vast.Identifier(out))
    pr1 = vast.PortArg(None, vast.Identifier(in1))
    pr2 = vast.PortArg(None, vast.Identifier(in2))
    ary = vast.Instance("or", "", (pr0, pr1, pr2), tuple([]))
    ark = vast.InstanceList("or", tuple([]), tuple([ary]))
    return ark


def mkAnd(in1, in2, out):
    pr0 = vast.PortArg(None, vast.Identifier(out))
    pr1 = vast.PortArg(None, vast.Identifier(in1))
    pr2 = vast.PortArg(None, vast.Identifier(in2))
    ary = vast.Instance("and", "", (pr0, pr1, pr2), tuple([]))
    ark = vast.InstanceList("and", tuple([]), tuple([ary]))
    return ark


def dumpscr(fn, fout):
    aag = read_Aag_struc(fn)
    jk = aag2cell(aag)
    codegen = ASTCodeGenerator()
    vout = codegen.visit(jk)
    with open(fout, 'w') as f:
        f.write(vout)
