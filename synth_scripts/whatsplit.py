import os
import re
from itertools import chain
from collections import Counter
import math
import pyverilog
from pyverilog.vparser.ast import InstanceList
from pyverilog.vparser.parser import parse
import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

prims = ["and", "buf", "not", "or", "nand", "nor"]


def get_args(input_string):
    return re.search(r'\((.*?)\)', input_string).group(1)  # type: ignore


def gatelines(filename):
    with open(filename, 'r') as file:
        return [line for line in file if "dout" in line]


def get_instances(fn):
    jx, _ = parse(fn)
    unwrap = jx.children()[0].children()[0].children()
    instances = [x for x in unwrap if type(x) == InstanceList]
    return instances


def pars_args(insts):
    gates = [{j.portname: j.argname for j in x.instances[0].children()}
             for x in insts]
    return gates


def subscript_cnt(gates) -> tuple[list[list], dict]:
    ins = chain.from_iterable(
        [v for i, v in xa.items() if i != "dout"]
        for xa in gates)
    total_count = dict(Counter(ins))
    word_count = {}
    gates2 = []
    for g in gates:
        nport = []
        for portn, argn in g.items():
            if (portn == "dout" or total_count[argn] < 2):
                nport.append((str(argn), 0))
            else:
                wc = word_count.get(str(argn), 0)
                nport.append((str(argn), wc))
                word_count[str(argn)] = wc + 1
        gates2.append(nport)
    return gates2, word_count


# def subscript_cnt(insts):
#     gates = [[(j.portname, j.argname) for j in x.instances[0].children()]
#          for x in insts]
#         gates = [ for j in x.instances[0].children()]
#     ins = chain.from_iterable(
#         xa[1:] if str(xa.module) in prims else
#         [v for i, v in xa.items() if i != "dout"]
#         for xa in insts)
#     total_count = dict(Counter(ins))
#     word_count = {}
#     gates2 = []
#     for x in insts:
#         gates = [(j.portname, j.argname) for j in x.instances[0].children()]
#         if  str(x.module) in prims:
#             vls = [j.argname for j in x.instances[0].children()]
#             nport = [(str(vls[0]), 0)]
#             for argn in vls[1:]:
#                 if (total_count[argn] < 2):
#                     nport.append((str(argn), 0))
#                 else:
#                     wc = word_count.get(str(argn), 0)
#                     nport.append((str(argn), wc))
#                     word_count[str(argn)] = wc + 1
#             gates2.append(nport)
#     return gates2, word_count


def showgate(gate, wcount, inst: vast.Instance):
    frontgate = inst.module
    pnames = [j.portname for j in inst.children()]
    gtype = str(frontgate)
    gate = [v if (p == "dout")
            else v+(prefix_free(wc, wcount.get(v, 0))[:-1])
            for p, (v, wc) in zip(pnames, gate)]
    gate = [vast.PortArg(p, vast.Identifier(v)) for p, v in zip(pnames, gate)]
    ary = vast.Instance(gtype, inst.name, tuple(gate), tuple([]))
    # ary = vast.Instance(gtype, f"g{index}" if (gtype not in prims) else "", tuple(gate), tuple([]))
    ark = vast.InstanceList(gtype, tuple([]), tuple([ary]))
    return ark


def split_from_file(fnin):
    base_name, extension = os.path.splitext(fnin)
    fnout = base_name + "_spl" + extension
    jx, _ = parse([fnin])
    unwrap = jx.children()[0].children()[0].children()
    insts = [x for x in unwrap if type(x) == InstanceList]
    rest = [x for x in unwrap if type(x) != InstanceList]
    spinsts = fixedgates(insts)
    mod = vast.ModuleDef("mymod", None, rest[1], rest[2:] + spinsts[0] + spinsts[1])
    codegen = ASTCodeGenerator()
    vout = codegen.visit(mod)
    with open(fnout, 'w') as f:
        f.write(vout)


def fixedgates(insts):
    gates = pars_args(insts)
    gates2, wcount = subscript_cnt(gates)
    base = [showgate(g, wcount, insts[i].instances[0]) for i, g in enumerate(gates2)]
    spl = [wholesplt(groot, N) for groot, N in wcount.items()]
    spliters = list(chain.from_iterable(spl))
    new_wires = [[vast.Wire(str(groot)+suf)
                 for suf in displit('_spl_', 0, N-1)]
                 for groot, N in wcount.items()]
    new_wires = list(chain.from_iterable(new_wires))
    return new_wires, base + spliters


def wholesplt(groot, N):
    if (N == 1):
        return []
    return [mksplt(groot, n) for n in displit('_spl_', 0, N-1)]


def mksplt(groot, suffix):
    groot = str(groot)
    dout = groot + suffix
    din = groot + (suffix != '_spl_')*suffix[:-1]
    j = mkSplBuf(din, dout)
    return j


def prefix_free(n, N):
    if (N == 0):
        return ''
    lnth = N.bit_length()
    pot = 2 ** (lnth - 1) if N > 0 else 0
    if (n < 2*(N-pot)):
        return "_spl_"+bin(n)[2:].zfill(lnth)
    else:
        return "_spl_"+bin(n+pot-N)[2:].zfill(lnth-1)


def dbg_pfree(n):
    return [prefix_free(i, n) for i in range(n)]


def splat(n):
    lnth = n.bit_length()
    pohigh = 2 ** lnth if n > 0 else 0
    polow = 2 ** (lnth - 1) if n > 0 else 0
    hright = max(n-polow, polow//2)
    # hright = min(pohigh-n, polow//2)
    hleft = n - hright
    return hleft


def displit(n: str, low: int, high: int) -> list[str]:
    if (low == high):
        return []
    size = high - low + 1
    mid = splat(size) + low - 1
    if (mid == high):
        __import__('pdb').set_trace()
        raise Exception("mid == high")
    return [n] + displit(n+"0", low, mid) + displit(n+"1", mid+1, high)

def mkSplBuf(net, nout=None):
    inp = vast.PortArg("din", vast.Identifier(net))
    outp = vast.PortArg("dout", vast.Identifier(nout))
    ary = vast.Instance("splt", f"g{net}", (outp, inp), tuple([]))
    ark = vast.InstanceList("splt", tuple([]), tuple([ary]))
    return ark
