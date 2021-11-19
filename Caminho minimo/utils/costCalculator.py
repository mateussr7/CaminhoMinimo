from typing import List


def calc_cost(dist: List[int], target):
    return dist[target]


def calc_cost_from_matrix(dist: List[List[int]], path: List[int]):
    cost = 0
    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]

    return cost
