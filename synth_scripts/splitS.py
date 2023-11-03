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


def get_instances(fn):
    jx, _ = parse(fn)
    unwrap = jx.children()[0].children()[0].children()
    instances = [x for x in unwrap if type(x) == InstanceList]
    return instances


def pars_args(insts):
    gates = [[j.argname for j in x.instances[0].children()]
             for x in insts]
    frontgate = [x.instances[0].module for x in insts]
    return gates, frontgate


def subscript_cnt(gates):
    ins = chain.from_iterable(
        xa[1:]
        for xa in gates)
    total_count = dict(Counter(ins))
    word_count = {}
    gates2 = []
    for vls in gates:
        nport = [(str(vls[0]), 0)]
        for argn in vls[1:]:
            if (total_count[argn] < 2):
                nport.append((str(argn), 0))
            else:
                wc = word_count.get(str(argn), 0)
                nport.append((str(argn), wc))
                word_count[str(argn)] = wc + 1
        gates2.append(nport)
    return gates2, word_count


def showgate(gate, index, wcount, frontgate):
    gate = [v if (i == 0)
            else v+(prefix_free(wc, wcount.get(v, 0))[:-1])
            for i, (v, wc) in enumerate(gate)]
    gate = [vast.PortArg(None, vast.Identifier(v)) for v in gate]
    ary = vast.Instance(frontgate[index], "", tuple(gate), tuple([]))
    ark = vast.InstanceList(frontgate[index], tuple([]), tuple([ary]))
    return ark


def split_from_file(fn):
    insts = get_instances(fn)
    return fixedgates(insts)


def fixedgates(insts):
    gates, frontgate = pars_args(insts)
    gates2, wcount = subscript_cnt(gates)
    base = [showgate(g, i, wcount, frontgate) for i, g in enumerate(gates2)]
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
    inp = vast.PortArg(None, vast.Identifier(net))
    outp = vast.PortArg(None, vast.Identifier(nout))
    ary = vast.Instance("buf", "", (outp, inp), tuple([]))
    ark = vast.InstanceList("buf", tuple([]), tuple([ary]))
    return ark
