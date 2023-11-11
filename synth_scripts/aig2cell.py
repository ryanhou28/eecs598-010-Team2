import os
import dill
from itertools import chain
import aiger as ag
from aiger import AIG
from backphase import Aag
from apply_backphase import Nettype, aag_to_nettype
import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
from splitS import fixedgates2
from readaig import read_Aag_struc
from itertools import cycle
from toplse import tocell


map_dict = {"and": "LA", "or": "FA", "buf": "SP"}


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


def aag2cell(aag: Aag, L_cnt: int = 0,
             Non_dbg: bool = False, levels: list[int] = []):
    gater = mkDefault if Non_dbg else mkBuiltin
    nets, phase = aag_to_nettype(aag)
    out_cnt = aag.out_cnt
    in_cnt = aag.in_cnt
    out_lut = aag.out_lut
    dro_lut = []
    in_names = aag.in_names
    out_names = aag.out_names
    if (Non_dbg and L_cnt > 0):
        out_cnt = out_cnt - L_cnt
        in_cnt = in_cnt - L_cnt
        dro_lut = out_lut[out_cnt:]
        out_lut = out_lut[:out_cnt]
        in_names = in_names[:in_cnt]
        out_names = out_names[:out_cnt]
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
    for i in range(in_cnt):
        nods[2 * (i+1)] = in_names[i]+"_p"
        nods[2 * (i+1) + 1] = in_names[i]+"_n"
    for i in range(L_cnt):
        y = i + in_cnt
        nods[2 * (y+1)] = f"ffc_{i}_p"
        nods[2 * (y+1) + 1] = f"ffc_{i}_n"
    for x in in_names:
        if (not Non_dbg):
            declst_i.append(vast.Input(x))
            prtlst.append(vast.Port(x, None, None, None))
            padlist.append(mkBuf(x))
            padlist.append(mkInv(x))
        else:
            declst_i.append(vast.Input(x+"_p"))
            declst_i.append(vast.Input(x+"_n"))
            prtlst.append(vast.Port(x+"_p", None, None, None))
            prtlst.append(vast.Port(x+"_n", None, None, None))
    for i, x in enumerate(out_names):
        suffix = "_n" if phase[i] else "_p"
        x += Non_dbg*suffix
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
                gatlist.append(gater("and", [nods[pga], nods[pb], nods[pa]]))
            case Nettype.OR:
                gatlist.append(gater("or", [nods[nga], nods[nb], nods[na]]))
            case Nettype.PAIR:
                gatlist.append(gater("and", [nods[pga], nods[pb], nods[pa]]))
                gatlist.append(gater("or", [nods[nga], nods[nb], nods[na]]))
    for out_ind, (po, out_pol) in enumerate(out_lut):
        if (not Non_dbg):
            pol = (out_pol ^ phase[out_ind])
            gatype = mkInv if phase[out_ind] else mkBuf
            oname = out_names[out_ind]
            lastout = gatype(nods[2 * po + pol], oname)
            ouch.append(lastout)
        else:
            pol = (out_pol ^ phase[out_ind])
            suf = "_n" if phase[out_ind] else "_p"
            oname = out_names[out_ind]+suf
            # TODO: make assignment for non-debug
            # That would cause an issue since splitter insertion
            # does not recognise nets in assigns
            lastout = mkBuf(nods[2 * po + pol], oname)
            ouch.append(lastout)
    for dro_ind, (co, ff_pol) in enumerate(dro_lut):
        lvl = levels[out_cnt+dro_ind]
        out_ind = dro_ind + out_cnt
        pol = (ff_pol ^ phase[out_ind])
        droc_pol = phase[out_ind]
        lastout = mkDROC(nods[2 * co + pol], dro_ind, droc_pol, lvl)
        ouch.append(lastout)
    wirelist = [vast.Wire(x) for x in nods.values()]
    wirelist = wirelist[2:]
    instlist = gatlist+ouch
    spl_wires, spliters = fixedgates2(instlist)
    mod = vast.ModuleDef("mymod", None, ports, [dec_i, dec_o]
                         + wirelist + spl_wires + padlist + spliters)
    if Non_dbg:
        d_i = [str(x.name) for x in declst_i]
        d_o = [str(x.name) for x in declst_o]
        twosp = twosplit(spliters, levels[out_cnt:])
        return mod, (d_i, d_o, twosp)
    else:
        return mod, ()
    # return mod, tocell(d_i, d_o, twosp)


def mkDROC(net, index, polarity, lvl):
    nout = f"ffc_{index}"
    s_p, s_n = "_p", "_n"
    if (polarity):
        s_p, s_n = s_n, s_p
    args = [("doutp", nout+s_p), ("doutn", nout+s_n), ("din", net)]
    return mkGate("DROC", args, f"{nout}_{lvl}")


def mkInv(net, nout=None):
    if (nout is None):
        nout = net + "_n"
    return mkBuiltin("not", [nout, net])


def mkBuf(net, nout=None):
    if (nout is None):
        nout = net + "_p"
    return mkBuiltin("buf", [nout, net])


def mkOr(in1, in2, out):
    return mkBuiltin("or", [out, in1, in2])


def mkAnd(in1, in2, out):
    return mkBuiltin("and", [out, in1, in2])


def mkDefault(type: str, args: list[str]):
    type = map_dict[type]
    inz = ["din"] if len(args) == 2 else [
        f"din{i+1}" for i in range(len(args))]
    portnames = ["dout"] + inz
    gname = "g_"+args[0]
    return mkGate(type, list(zip(portnames, args)), gname)


def mkBuiltin(type: str, args: list[str]):
    return mkGate(type, list(zip(cycle([None]), args)))


def mkGate(type: str, args: list[tuple[str | None, str]], name: str = ""):
    ports = tuple([vast.PortArg(port_id, vast.Identifier(wire_id))
                   for port_id, wire_id in args])
    ary = vast.Instance(type, name, ports, tuple([]))
    ark = vast.InstanceList(type, tuple([]), tuple([ary]))
    return ark


def dumpscr(fn, fout, L_cnt=0, Non_dbg=False, levels=[]):
    aag = read_Aag_struc(fn)
    jk, pylse_list = aag2cell(aag, L_cnt, Non_dbg, levels)
    codegen = ASTCodeGenerator()
    vout = codegen.visit(jk)
    with open(fout, 'w') as f:
        f.write(vout)
    if Non_dbg:
        (inps, outs, glist) = pylse_list  # type: ignore
        n_lvl = max(levels+[0])
        pkpath = os.path.splitext(fout)[0] + '.' + 'pk'
        with open(pkpath, 'wb') as f:
            dill.dump((inps, outs, glist, n_lvl, levels), f)

def twosplit(insts, levels: list[int] = []):
    hmm = reorder_dros(insts, levels)
    levels.sort()
    nuhmm = [[]]
    drohm = []
    in_use = {}
    out_pos = {}
    for i, (nm, pa) in enumerate(hmm):
        if (nm != "DROC"):
            inpa = pa[1:]
        else:
            inpa = pa[2:]
        nuinpa = []
        for aa in inpa:
            if (not aa.__contains__("_spl_")):
                nuinpa.append(aa)
            elif (aa not in in_use):
                in_use[aa] = i
                nuinpa.append(aa+"_a")
            else:
                nuinpa.append(aa+"_b")
        if (not pa[0].__contains__("_spl_")):
            if (nm != "DROC"):
                nuout = pa[0:1]
                out_pos[pa[0]] = i+1
                nuhmm.append([(nm, nuout, nuinpa)])
            else:
                nuout = pa[0:2]
                out_pos[pa[0]] = i+1
                out_pos[pa[1]] = i+1
                og_wire = pa[-1].split("_spl_")[0]
                posx = out_pos.get(og_wire, 0)
                drohm.insert(0, (i+1, posx))
                lvlclk = f"clk_{levels[0]}"
                levels = levels[1:]
                nuhmm.append([(nm, nuout, nuinpa+[lvlclk])])
        else:
            nuout = [pa[0]+"_a", pa[0]+"_b"]
            og_wire = pa[0].split("_spl_")[0]
            posx = out_pos.get(og_wire, 0)
            nuhmm[posx].append(("spl", nuout, nuinpa))
    for src, loc in drohm:
        nuhmm[loc] += nuhmm[src]
        nuhmm[src] = []
    nuhmm = list(chain.from_iterable(nuhmm))
    return nuhmm


def reorder_dros(insts, levels: list[int]=[]):
    dro_locations = []
    for i, x in enumerate(insts):
        if (str(x.module) == "DROC"):
            dro_locations.append(i)
    dro_buckets = [[] for _ in range(len(set(levels)))]
    for i, x in zip(dro_locations, levels):
        dro_buckets[x].append(i)
    bucks = list(chain.from_iterable(dro_buckets))
    b_dict = {src: loc for src, loc in zip(dro_locations, bucks)}
    new_locs = [b_dict.get(i, i) for i in range(len(insts))]
    hmm = [(insts[i].module, [str(y.argname)
            for y in insts[i].instances[0].children()]) for i in new_locs]
    return hmm
