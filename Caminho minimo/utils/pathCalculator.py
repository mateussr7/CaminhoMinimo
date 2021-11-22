from typing import List


def calc_best_path(pred: List[int], source, target):
    if source == target:
        return []

    path: List[int] = []

    p = target
    while p != source:
        path.insert(0, p)
        p = pred[p]

    path.insert(0, source)
    return path


def calc_best_path_from_matrix(pred: List[List[int]], s: int, t: int):
    path: List[int] = [t]
    aux = t
    while aux != s:
        aux = pred[s][aux]
        path.insert(0, aux)
    return path
