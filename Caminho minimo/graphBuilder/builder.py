from graph import Graph


def build_graph(file_name) -> Graph:
    full_path = "store/" + file_name
    with open(full_path) as file:
        stats = file.readline()
        vertexes, edges = stats.split()
        graph = Graph(int(vertexes), int(edges))

        lines = file.readlines()
        for values in lines:
            s, t, w = values.split()
            graph.add_edge(int(s), int(t), int(w))

        file.close()
        return graph
