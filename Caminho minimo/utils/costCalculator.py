from typing import List


def calc_cost(dist: List[int], target):
    return dist[target]


def calc_cost_from_matrix(dist: List[List[int]], source: int, target: int):
    return dist[source][target]
