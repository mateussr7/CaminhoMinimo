from graph import Graph
import numpy as np


def build_graph(file_name, source, target) -> Graph:
    full_path = "store/" + file_name
    with open(full_path) as file:
        stats = file.readline()
        vertexes, edges = stats.split()
        graph = Graph(int(vertexes), int(edges))

        lines = file.readlines()
        for values in lines:
            s, t, w = values.split()
            graph.add_edge(int(s), int(t), int(w))

        graph_final = np.asarray(graph.G)
        file.close()
        return graph
