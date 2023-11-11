from itertools import chain
from collections import Counter
# import pyverilog
from pyverilog.vparser.ast import InstanceList
from pyverilog.vparser.parser import parse
import pyverilog.vparser.ast as vast


def get_instances(fn):
    jx, _ = parse(fn)
    unwrap = jx.children()[0].children()[0].children()
    instances = [x for x in unwrap if type(x) == InstanceList]
    return instances


# def pars_args(insts):
#     gates = [[j.argname for j in x.instances[0].children()]
#              for x in insts]
#     frontgate = [x.instances[0].module for x in insts]
#     return gates, frontgate


def input_args(inst: InstanceList):
    ports = inst.instances[0].children()[1:]
    inargs = [str(j.argname) for j in ports
              if not str(j.portname).__contains__("out")]
    return inargs


def fixedgates2(insts):
    """
    Assumptions: 1st port in gate is output,
    named output ports have 'out' in name
    """
    inp_args = [input_args(x) for x in insts]
    ins = chain.from_iterable(inp_args)
    total_count = dict(Counter(ins))
    word_count = {}
    gates2 = []
    for gate in insts:
        plist = []
        gports = gate.instances[0].children()
        for i, port in enumerate(gports):
            argn = str(port.argname)
            porn = str(port.portname)
            tot_cnt = total_count.get(argn, 0)
            occ_cnt = word_count.get(argn, 0)
            # if current port is output
            if porn.__contains__("out") or i == 0:
                nuname = argn
            # if current port's wire is not shared so not from splitter
            elif (tot_cnt < 2):
                nuname = argn
            else:
                nuname = argn+(prefix_free(occ_cnt, tot_cnt)[:-1])
                word_count[argn] = occ_cnt + 1
            plist.append((port.portname, nuname))
        oldname = gate.instances[0].name
        nugate = mkGate(gate.module, plist, oldname)
        gates2.append(nugate)
    spl = [wholesplt(groot, N) for groot, N in total_count.items()]
    spliters = list(chain.from_iterable(spl))
    assert (all(word_count[i] == total_count[i] for i in word_count.keys()))
    new_wires = [[vast.Wire(str(groot)+suf)
                 for suf in displit('_spl_', 0, N-1)]
                 for groot, N in total_count.items()]
    new_wires = list(chain.from_iterable(new_wires))
    return new_wires, gates2 + spliters
    # return gates2, word_count


# def showgate(gate, index, wcount, frontgate):
#     gate = [v if (i <= 0)
#             else v+(prefix_free(wc, wcount.get(v, 0))[:-1])
#             for i, (v, wc) in enumerate(gate)]
#     gate = [vast.PortArg(None, vast.Identifier(v)) for v in gate]
#     ary = vast.Instance(frontgate[index], "", tuple(gate), tuple([]))
#     ark = vast.InstanceList(frontgate[index], tuple([]), tuple([ary]))
#     return ark


def split_from_file(fn):
    insts = get_instances(fn)
    return fixedgates2(insts)


# def fixedgates(insts: list[InstanceList]
#                ) -> tuple[list[Wire], list[InstanceList]]:
#     """
#     Given a list of gates instances return the list including required
#     splitters and the additional wire declarations.
#     """
#     gates, frontgate = pars_args(insts)
#     gates2, wcount = subscript_cnt(gates)
#     base = [showgate(g, i, wcount, frontgate) for i, g in enumerate(gates2)]
#     spl = [wholesplt(groot, N) for groot, N in wcount.items()]
#     spliters = list(chain.from_iterable(spl))
#     new_wires = [[vast.Wire(str(groot)+suf)
#                  for suf in displit('_spl_', 0, N-1)]
#                  for groot, N in wcount.items()]
#     new_wires = list(chain.from_iterable(new_wires))
#     return new_wires, base + spliters


def wholesplt(groot: str, N: int) -> list[InstanceList]:
    "Create all splitters for the fanout of groot with N leaves"
    if (N == 1):
        return []
    return [mksplt(groot, n) for n in displit('_spl_', 0, N-1)]


def mksplt(groot: str, suffix: str) -> InstanceList:
    "Wrapper to create splitter from name root and suffix"
    dout = groot + suffix
    din = groot + (suffix != '_spl_')*suffix[:-1]
    return mkSplBuf(din, dout)


def prefix_free(n, N):
    "The splitter suffix of the n-th instance of a wire with N occurances"
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


def splat(n: int) -> int:
    "A splitter with n leaves delegates splat(n) to the left subtree"
    lnth = n.bit_length()
    # pohigh = 2 ** lnth if n > 0 else 0
    polow = 2 ** (lnth - 1) if n > 0 else 0
    hright = max(n-polow, polow//2)
    # hright = min(pohigh-n, polow//2)
    hleft = n - hright
    return hleft


def displit(n: str, low: int, high: int) -> list[str]:
    "Returns suffixes of splitter and it's subsplitters"
    if (low == high):
        return []
    size = high - low + 1
    mid = splat(size) + low - 1
    if (mid == high):
        __import__('pdb').set_trace()
        raise Exception("mid == high")
    return [n] + displit(n+"0", low, mid) + displit(n+"1", mid+1, high)


def mkSplBuf(net: str, nout: str) -> InstanceList:
    # inp = vast.PortArg(None, vast.Identifier(net))
    # outp = vast.PortArg(None, vast.Identifier(nout))
    # ary = vast.Instance("buf", "", (outp, inp), tuple([]))
    # ark = vast.InstanceList("buf", tuple([]), tuple([ary]))
    return mkGate("buf", [(None, nout), (None, net)])


def mkGate(type: str, args: list[tuple[str | None, str]], name: str = ""):
    ports = tuple([vast.PortArg(port_id, vast.Identifier(wire_id))
                   for port_id, wire_id in args])
    ary = vast.Instance(type, name, ports, tuple([]))
    ark = vast.InstanceList(type, tuple([]), tuple([ary]))
    return ark
