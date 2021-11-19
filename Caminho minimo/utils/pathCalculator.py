from typing import List


def revert_path(path: List[int]):
    new_path: List[int] = []
    i = len(path) - 1
    while i != -1:
        new_path.append(path[i])
        i -= 1

    return new_path


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
