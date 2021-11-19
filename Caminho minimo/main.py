import numpy
from utils import timeExecution
import time

from graph import Graph
from utils.pathCalculator import calc_best_path, revert_path, calc_best_path_from_matrix
from utils.timeExecution import TimeExecution
from graphBuilder.builder import build_graph
from utils.costCalculator import calc_cost, calc_cost_from_matrix
import numpy as np

#file_name = input("Informe o nome do arquivo contendo o grafo a ser processado: (O Arquivo deve estar dentro da pasta Store do codigo): ")
#algorithm_name = input("Qual algoritmo deve ser usado? (DIJKSTRA, BELLMAN_FORD ou FLOYD_WARSHAL): ")
#source_vertex = input("Informe o Vértice de origem: ")
#target_vertex = input("Informe o Vértice de destino: ")

target_vertex = 100
g = build_graph("facebook_combined.txt", 0, 100)

print("Inicializando algoritmo...")
time_execution = TimeExecution(time.time())
dist, pred = g.floyd_warshall()
time_execution.set_finish_time(time.time())
final_time = time_execution.calc_execution_time()
path = calc_best_path_from_matrix(pred, 0, 100)
print("Algoritmo executado em", round(final_time, 5), "segundos, com custo de", calc_cost_from_matrix(dist, path))
