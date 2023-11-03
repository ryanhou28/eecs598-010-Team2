import re
from typing import Dict, Tuple, Any, cast
from dataclasses import dataclass
import random
import numpy as np
import numpy.typing as npt
import os
import networkx as nx
import matplotlib.pyplot as plt
from trplot import add_partition_attribute
import aiger as ag
from aiger import AIG


def aig2aag(fn: str):
    "read aig to aag then read aag"
    root, ext = os.path.splitext(fn)
    assert ext == ".aig"
    print(f"X_{fn}")
    aig = ag.load(fn)
    print(f"A_{fn}")
    out = root + ".aag"
    aig.write(out)
    rename_aagouts(out)


def parse_aag(f) -> Tuple[Tuple[int, int, int], nx.DiGraph]:
    raw = aaglist(f)
    head = raw[0]
    _, ins, _, outs, ncnt = head
    init = ins+outs+1
    ouch = raw[ins+1:init]
    nodes = raw[init:init+ncnt]
    G = nx.DiGraph()
    G.add_nodes_from(range(1, ins+ncnt+outs+1))
    for i, a, b in nodes:
        G.add_edge(a//2, i//2, value=a % 2)
        G.add_edge(b//2, i//2, value=b % 2)
    y = ins+ncnt+1
    for i, x in enumerate(ouch):
        G.add_edge(x[0]//2, y+i, value=x[0] % 2)
    return (ins, outs, ncnt), G


@dataclass
class Aag:
    """
    AIG as represented with indexes in native format.
    nodes is in topological order.
    """
    in_cnt: int
    out_cnt: int
    node_cnt: int
    nodes: Dict[int, Tuple[Tuple[int, int], Tuple[int, int]]]
    out_lut: list[Tuple[int, int]]
    in_names: list[str]
    out_names: list[str]


def read_Aag_struc(filename: str) -> Aag:
    """
    Parse .aag file to Aag instance
    Turn the numbers from the .aag file
    to Aag struct.
    Nodes in .aag are already in topological order,
    so they are in Aag.nodes too.
    """
    raw = []
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = re.findall(r'\b\d+\b', line)
            raw.append(list(map(int, numbers)))
            lines.append(line)

    head = raw[0]
    _, ins, _, outs, ncnt = head
    init = ins+outs+1
    ouch = raw[ins+1:init]
    out_lut = [(n[0]//2, n[0] % 2) for n in ouch]
    nodes = raw[init:init+ncnt]
    nodes = {node//2:
             (((in1//2), (in1 % 2)),
              ((in2//2), (in2 % 2)))
             for node, in1, in2 in nodes}
    name_lines = lines[init+ncnt:init+ncnt+ins+outs]
    names = [lin.split()[1] for lin in name_lines]
    in_names = names[:ins]
    out_names = names[ins:]
    return Aag(ins, outs, ncnt, nodes, out_lut, in_names, out_names)


def aaglist(filename: str) -> list[list[int]]:
    """
    The numbers that define the AIG
    in the .aag text file
    """
    numbers_list = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = re.findall(r'\b\d+\b', line)
            numbers_list.append(list(map(int, numbers)))
    return numbers_list


def paint(G):
    edge_attributes = nx.get_edge_attributes(G, 'value')
    add_partition_attribute(G)
    pos = nx.multipartite_layout(G, subset_key="partition")
    nx.draw(G, pos, with_labels=True, node_size=5,
            node_color='blue', font_size=17)
    nx.draw_networkx_edge_labels(G, pos,
                                 edge_labels=edge_attributes, font_size=8)
    pol = naive_pol(G)
    nx.draw_networkx_labels(G, pos, labels=pol, font_size=8, font_color="red")
    plt.show()


def paintd(G):
    add_partition_attribute(G)
    pos = nx.multipartite_layout(G, subset_key="partition")
    nx.draw(G, pos, with_labels=False, node_size=5, node_color='blue')
    # nx.draw_networkx_edge_labels(G, pos,
    # edge_labels=edge_attributes, font_size=8)
    # pol = naive_pol(G)
    ppol = {}
    for g in G.nodes():
        ppol[g] = f"{g//2}_{g%2}"
    nx.draw_networkx_labels(G, pos, labels=ppol,
                            font_size=14, font_color="red")
    plt.show()
    # return pos


def naive_pol(G: nx.DiGraph) -> Dict[int, Tuple[bool, bool]]:
    "Polarity of each node of aig as graph given all positive/initial \
    phase assignment for all outputs"
    # Create a dictionary to store computed attributes for each node
    computed_attributes = {}
    # Iterate through the nodes in reverse topological order
    for node in reversed(list(nx.topological_sort(G))):
        # If the node has no outgoing edges (output node),
        # set its initial attribute
        if G.out_degree(node) == 0:
            computed_attributes[node] = (True, False)  # Change this as needed
            # Iterate through ingoing edges and update the attribute
        hm = G.in_edges(node, data='value')  # type: ignore
        for j in hm:
            sourc, _, edge_data = cast(tuple[Any, Any, Any], j)
            # Modify this step to compute the attribute based
            # on edge and target node attributes
            if sourc not in computed_attributes:
                computed_attributes[sourc] = (False, False)
            (pa, na) = computed_attributes[node]
            (pa, na) = (na, pa) if (edge_data == 1) else (pa, na)
            (pb, nb) = computed_attributes[sourc]
            computed_attributes[sourc] = (pb or pa, nb or na)
    # Assign computed attributes back to the input nodes
    # for node, attributes in computed_attributes.items():
        # G.nodes[node]['pol'] = attributes
    return computed_attributes


# ----
# Duplication
def dup(G: nx.DiGraph) -> nx.DiGraph:
    pol = naive_pol(G)
    DG = nx.DiGraph()
    for a, b, d in G.edges.data('value'):  # type: ignore
        (pt, nt) = pol[b]
        ed = (d == 0)
        if (pt and ed):
            DG.add_edge(2*a, 2*b)
        if (pt and not ed):
            DG.add_edge(2*a+1, 2*b)
        if (nt and ed):
            DG.add_edge(2*a+1, 2*b+1)
        if (nt and not ed):
            DG.add_edge(2*a, 2*b+1)
    return DG


def make_naive_dual(fn):
    "Create and save the naive/bubble-push dual of aig in file fn"
    out = os.path.splitext(fn)[0] + "_naive.aag"
    _, daig = getboth(fn)
    daig.write(out)


def dup2ai(DG: nx.DiGraph) -> AIG:
    "Construct an aig from bubble-pushed dual graph"
    # node even and odd or
    # outs in order index ithink so outi = n/2
    nods = {}
    ouch = {}
    nods[0] = ag.atom(False)
    nods[1] = ag.atom(True)
    for node in list(nx.topological_sort(DG)):
        if (node <= 1):
            continue
        j = [x for x, _ in DG.in_edges(node)]  # type: ignore
        match j:
            case []:
                nods[node] = ag.atom(f"i{node//2}_{node%2}")
            case [x]:
                ouch[node] = (nods[x])
            case [a, b]:
                if (node % 2 == 0):
                    nods[node] = nods[a] & nods[b]
                else:
                    nods[node] = nods[a] | nods[b]
    return merge_outs(ouch)


def merge_outs(ouch):
    "Combines aig expressions of all outputs to one aig"
    # Outputs are assigned ids in the order of their node id
    # Works if original aig's outputs also followed that rule
    ouch = [v.with_output(f"o{i}").aig
            for i, (_, v) in enumerate(sorted(ouch.items()))]
    x = ouch[0]
    # |ing aigs (instead of their expressions) combines the networks/outputs
    for h in ouch[1:]:
        x = x | h
    return x


def mono_inps(daig: AIG) -> AIG:
    "Turns dual inputs duped aig to single inputed, gates remain unchanged"
    inz = {x.split("_")[0] for x in daig.inputs}
    baig = daig
    for inp in inz:
        baig = ag.source({f"{inp}_1": ag.atom(f"{inp}_0")}) >> baig
    return baig


def simdual(aig, binary_number):
    "Evaluate dual aig on inputs formated as binary string"
    nkeys = len(aig.inputs)
    keys = [f"i{n//2+1}_{n%2}" for n in range(nkeys)]
    dualin = []
    for bit in binary_number:
        if bit == '0':
            dualin.extend([False, True])
        elif bit == '1':
            dualin.extend([True, False])
    inputdict = dict(zip(keys, dualin))
    return aig(inputdict)[0]


def simsingle(aig, binary_number):
    "Evaluate single aig on inputs formated as binary string"
    nkeys = len(aig.inputs)
    keys = [f"i{n}" for n in range(nkeys)]
    dualin = []
    for bit in binary_number:
        if bit == '0':
            dualin.append(False)
        elif bit == '1':
            dualin.append(True)
    inputdict = dict(zip(keys, dualin))
    return aig(inputdict)[0]


def simboth(aig, daig, bn):
    return simsingle(aig, bn), simdual(daig, bn)


def sample_bits(n):
    "Return a string of n random bits"
    random_string = ''.join(random.choice(['0', '1']) for _ in range(n))
    return random_string


def check1(aig, daig):
    """Simulate both single and bubble-pushed AIG
    and compare simulation results to confirm equivalance"""
    n = len(aig.inputs)
    no = len(aig.outputs)
    aper = [f"o{i}" for i in range(no)]
    a, b = simboth(aig, daig, sample_bits(n))
    a = np.array([a[i] for i in aper])
    b = np.array([b[i] for i in aper])
    return all(a == b)


def checksingledual(aig, daig, n):
    return all(check1(aig, daig) for _ in range(n))


def getboth(fn):
    "Return aig from a file and it's bubble-pushed duplicate"
    aig = ag.load(fn)
    _, G = parse_aag(fn)
    DG = dup(G)
    daig = dup2ai(DG)
    return aig, daig


def rename_aagouts(fn):
    """Put output names in order in generated .aag file
    such that output order matches name order. """
    with open(fn, 'r') as file:
        lines = file.readlines()
    edited_lines = []
    for line in lines:
        if line.startswith('o') or line.startswith('i'):
            words = line.strip().split()
            if words:
                edited_lines.append(words[0] + ' ' + words[0] + '\n')
            else:
                edited_lines.append(line)
        else:
            edited_lines.append(line)
    with open(fn, 'w') as file:
        file.writelines(edited_lines)
