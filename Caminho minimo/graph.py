from typing import List, Tuple
from queue import PriorityQueue


class Graph:

    def __init__(self, vertexes, edges):
        self.G = [[0 for i in range(vertexes)] for j in range(vertexes)]
        self.vertexes = vertexes
        self.edges = edges

    def add_edge(self, source, target, weight):
        self.G[source][target] = self.G[target][source] = weight

    def dijkstra(self, s: int):
        dist: List[float] = [float('inf') for v in range(self.vertexes)]  # precisa ser float pois int nao aceita o valor "infinito"
        pred: List[int] = [None for v in range(self.vertexes)]

        dist[s] = 0
        q = PriorityQueue()
        q.put((0, s))

        while not q.empty():
            u: Tuple[int, int] = q.get()
            distance = u[0]
            vertex = u[1]
            if distance > dist[vertex]:
                continue

            adjacent: List[Tuple[int, int]] = [(c, n) for c, n in enumerate(self.G[vertex]) if n != 0]
            for v, w in adjacent:
                if dist[v] > dist[vertex] + w:
                    dist[v] = dist[vertex] + w
                    pred[v] = vertex
                    q.put((w, v))

        return dist, pred

    def bellman_ford(self, s: int):
        dist: List[float] = [float('inf') for v in range(self.vertexes)]
        pred: List[int] = [None for v in range(self.vertexes)]

        dist[s] = 0

        edges: List[Tuple[int, int, int]] = []

        for m in range(self.vertexes):
            for n in range(self.vertexes):
                if self.G[m][n] != 0:
                    edges.append((m, n, self.G[m][n]))

        for i in range(self.vertexes - 1):
            change = False
            for u, v, w in edges:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    change = True

            if not change:
                break

        return dist, pred

    def floyd_warshall(self):
        dist: List[List[float]] = [[float('inf') for v in range(self.vertexes)] for n in self.G]
        pred: List[List[int]] = [[None for v in range(self.vertexes)] for n in self.G]

        for i in range(len(self.G)):
            for j in range(len(self.G)):
                if i == j:
                    dist[i][j] = 0
                elif self.G[i][j] != 0:
                    dist[i][j] = self.G[i][j]
                    pred[i][j] = i
                else:
                    dist[i][j] = float('inf')
                    pred[i][j] = None

        for k in range(len(self.G)):
            for i in range(len(self.G)):
                for j in range(len(self.G)):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        pred[i][j] = pred[k][j]

        return dist, pred
