import networkx as nx


def add_partition_attribute(graph: nx.DiGraph):
    # Get a topological ordering of the nodes in the graph
    topological_order = list(nx.topological_sort(graph))
    # Initialize a dictionary to store distances from inputs
    distances = {node: 0 for node in topological_order}
    # Traverse the graph in topological order
    for node in topological_order:
        # Get the predecessors (inputs) of the current node
        predecessors = list(graph.predecessors(node))
        # Calculate the distance from inputs
        if predecessors:
            max_distance = max(distances[predecessor]
                               for predecessor in predecessors)
            distances[node] = max_distance + 1
    # Add the 'partition' attribute to each node
    for node, distance in distances.items():
        graph.nodes[node]['partition'] = distance
