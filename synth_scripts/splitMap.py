import re
from itertools import chain
from collections import Counter
import math
import pyverilog
from pyverilog.vparser.ast import InstanceList
from pyverilog.vparser.parser import parse
import pyverilog.vparser.ast as vast


def get_args(input_string):
    return re.search(r'\((.*?)\)', input_string).group(1)  # type: ignore


def gatelines(filename):
    with open(filename, 'r') as file:
        return [line for line in file if "dout" in line]


def pars_args(fn):
    jx, _ = parse(fn)
    unwrap = jx.children()[0].children()[0].children()
    gates = [{j.portname: j.argname for j in x.instances[0].children()}
             for x in unwrap if type(x) == InstanceList]
    frontgate = [f"{x.instances[0].module} {x.instances[0].name}"
                 for x in unwrap if type(x) == InstanceList]
    return gates, frontgate


def subscript_cnt(gates):
    ins = chain.from_iterable(
        [v for i, v in xa.items() if i != "dout"]
        for xa in gates)
    total_count = dict(Counter(ins))
    word_count = {}
    gates2 = []
    for g in gates:
        nport = {}
        for portn, argn in g.items():
            if (portn == "dout" or total_count[argn] < 2):
                nport[portn] = (str(argn), 0)
            else:
                wc = word_count.get(str(argn), 0)
                nport[portn] = (str(argn), wc)
                word_count[str(argn)] = wc + 1
        gates2.append(nport)
    return gates2, word_count


def showgate(gate, index, wcount, frontgate):
    gate = {k: v if (k == 'dout')
            else v+(prefix_free(wc, wcount.get(v, 0))[:-1])
            for k, (v, wc) in gate.items()}
    if (len(gate) == 3):
        return f"{frontgate[index]}(.dina({gate['dina']}), .dinb({gate['dinb']}), .dout({gate['dout']}));"
    else:
        return f"{frontgate[index]}(.din({gate['din']}), .dout({gate['dout']}));"


def fixedgates(fn):
    gates, frontgate = pars_args(fn)
    gates2, wcount = subscript_cnt(gates)
    base = '\n'.join(showgate(g, i, wcount, frontgate) for i, g in
                     enumerate(gates2))
    spl = [wholesplt(groot, N) for groot, N in wcount.items()]
    spl = chain.from_iterable(spl)
    spliters = '\n'.join(f'splt gs{i}' + bd for i, bd in enumerate(spl))
    new_wires = [[str(groot)+suf for suf in displit('_spl_', 0, N-1)]
                 for groot, N in wcount.items()]
    new_wires = chain.from_iterable(new_wires)
    new_wires = f"wire {', '.join(new_wires)};\n\n"
    return new_wires + base + '\n' + spliters


def wholesplt(groot, N) -> list[str]:
    if (N == 1):
        return []
    return [mksplt(groot, n) for n in displit('_spl_', 0, N-1)]


def mksplt(groot, suffix):
    groot = str(groot)
    dout = groot + suffix
    din = groot + (suffix != '_spl_')*suffix[:-1]
    j = f"(.din({din}), .dout({dout}));"
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


def mkAnd(in1, in2, out):
    pr0 = vast.PortArg("dina", vast.Identifier(in1))
    pr1 = vast.PortArg("dinb", vast.Identifier(in2))
    pr2 = vast.PortArg("dout", vast.Identifier(out))
    ary = vast.Instance("myand", "and2", (pr0, pr1, pr2), None)
    ark = vast.InstanceList("and2", None, tuple([ary]))
    return ark
