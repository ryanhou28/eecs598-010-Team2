from pylse import inp_at, inspect, Simulation
from pylse.circuit import InGen
from pylse import c_inv, c, s, jtl, dro_c, Wire, working_circuit
from copy import deepcopy
from collections import Counter
import pylse
import numpy as np


def fa(x, y, name):
    """
    First-arrival cell based on an inverted C-element.
    Inputs buffered with JTL for better flux transmission.
    """
    return c_inv(jtl(x), jtl(y), name)


def la(x, y, name):
    """
    Last-arrival cell based on a C-element.
    Inputs buffered with JTL for better flux transmission.
    """
    return c(jtl(x), jtl(y), name)


def tocell(inps, outs, gates, stage_cnt, levels):
    wires = {}
    levels.sort()
    clev = Counter(levels)
    clxz = [list(pylse.split(
            Wire(name=f"clk_{i}"), clev[i],
            None, firing_delay=0)) for i in range(stage_cnt)]
    for i, x in enumerate(inps):
        wires[x] = Wire(name=x)
    while len(gates) > 0:
        x = gates.pop(0)
        my_ins = x[2]
        if not all(x in wires or x.__contains__('clk_') for x in my_ins):
            gates.append(x)
            continue
        match x:
            case ('FA', [out], [in1, in2]):
                wires[out] = fa(wires[in1], wires[in2], out)
            case ('LA', [out], [in1, in2]):
                wires[out] = la(wires[in1], wires[in2], out)
            case ('spl', [out1, out2], [in1]):
                wires[out1], wires[out2] = s(wires[in1], out1, out2)
            case ('buf', [out], [in1]):
                wires[out] = jtl(wires[in1], out)
            case ('DROC', [outp, outn], [in1, clkx]):
                clk_id = int(clkx.split('_')[-1])
                my_clk = clxz[clk_id].pop()
                wires[outp], wires[outn] = dro_c(wires[in1], my_clk, outp, outn)
    return deepcopy(pylse.working_circuit())


def pylse_test(pkpath, tdatapath, delay: int = 1000):
    """
    pkpath: path to .pk file with stored arguments for tocell
    tdatapath: path to file with binary inputs for testbench,
    one sample per line
    delay: new input/clk delay

    Returns all results, list of primary output names,
    a numpy array of in which cycles each output had a pulse,
    and the deduplicated testbench results formated as a string
    to be compared to testbench results from original circuit in
    verilog.
    """
    working_circuit().reset()
    import dill
    with open(pkpath, 'rb') as f:
        j = dill.load(f)
    (inps, outs, glist, n_lvl, levels) = j
    wrap = tocell(*j)
    pre_samples = read_tdata(tdatapath)
    n_samp = len(pre_samples)
    duration = 2*n_samp+n_lvl
    clox = [[delay*(ci+1) + delay*n for n in range(2*n_samp)] for ci in range(n_lvl)]
    samples = []
    for x in pre_samples:
        xx = np.vstack([x,~x]).T.flatten()
        samples += [xx, np.logical_not(xx)]
    stimes = [[] for _ in inps]
    for i, samp in enumerate(samples):
        for ii, si in enumerate(samp):
            if (si):
                stimes[ii].append(i*delay+50)
    for st, nm in zip(stimes, inps):
        wrap.add_node(
            InGen(list(st)), [wrap.source_wire()],
            [wrap.get_wire_by_name(nm)])  # type: ignore
    for i, cllk in enumerate(clox):
        wrap.add_node(
            InGen(list(cllk)), [wrap.source_wire()],
            [wrap.get_wire_by_name(f"clk_{i}")])  # type: ignore
    sim = pylse.Simulation(wrap)
    events = sim.simulate()
    o_ev = [np.any([np.eye(duration)[int(i // delay)] for i in j], axis=0)
            for j in [events[o] for o in outs]]
    o_ev = np.array(o_ev).astype(int).T
    opol=np.array([x[-1]=="n" for x in outs])
    dut_out = o_ev[n_lvl:][::2]^opol
    dut_out = dut_out.astype(int).astype(str)
    dut_out = '\n'.join([''.join(row) for row in dut_out])
    return (events, outs, o_ev), dut_out


def num2lst(x, y):
    ll = []
    for _ in range(4):
        px, py = x % 2, y % 2
        ll += [px, 1 - px, py, 1 - py]
        x, y = x // 2, y // 2
    return ll


def read_tdata(file_name):
    binary_digits = []
    with open(file_name, 'r') as file:
        for line in file:
            binary_row = [int(digit) for digit in line.strip()]
            binary_digits.append(binary_row)
    binary_array = np.array(binary_digits)
    return binary_array.astype(bool)
