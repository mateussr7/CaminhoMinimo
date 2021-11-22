import sys
import time

from utils.pathCalculator import calc_best_path, calc_best_path_from_matrix
from utils.timeExecution import TimeExecution
from graphBuilder.builder import build_graph
from utils.costCalculator import calc_cost, calc_cost_from_matrix


file = input("Informe o numero equivalente ao arquivo contendo o grafo a ser processado: (1 - rg300_4730 || 2 - rome99c || 3 - facebook_combined || 4 - USA-road-dt.DC): ")
algorithm = input("Qual algoritmo deve ser usado? Digite o número correspondente(1 - DIJKSTRA || 2 - BELLMAN_FORD || 3 - FLOYD_WARSHAL): ")
num_algorithm = int(algorithm)
num_file = int(file)

if num_file > 4 or num_file < 1 or num_algorithm > 3 or num_algorithm < 1:
    print("Essa opção de arquivo/algoritmo nao existe! Tente novamente, digitando as opções numéricas dadas.")
    sys.exit(0)

source_vertex = input("Informe o Vértice de origem:")
source = int(source_vertex)
target_vertex = input("Informe o Vértice de destino:")
target = int(target_vertex)
print("\n\n")
file_name = ''
if file == '1':
    file_name = 'rg300_4730.txt'
elif file == '2':
    file_name = 'rome99c.txt'
elif file == '3':
    file_name = 'facebook_combined.txt'
elif file == '4':
    file_name = 'USA-road-dt.DC.txt'

g = build_graph(file_name)
time_execution = TimeExecution(time.time())
print("Inicializando algoritmo...")
cost = None
path = None

if algorithm == '1':
    dist, pred = g.dijkstra(source)
    time_execution.set_finish_time(time.time())
    cost = calc_cost(dist, target)
    path = calc_best_path(pred, source, target)

elif algorithm == '2':
    dist, pred = g.bellman_ford(source)
    time_execution.set_finish_time(time.time())
    cost = calc_cost(dist, target)
    path = calc_best_path(pred, source, target)

elif algorithm == '3':
    dist, pred = g.floyd_warshall()
    time_execution.set_finish_time(time.time())
    path = calc_best_path_from_matrix(pred, source, target)
    cost = calc_cost_from_matrix(dist, source, target)


rounded_time = round(time_execution.calc_execution_time(), 5)

print("Algoritmo executado em", rounded_time, "segundos, com custo de", cost)
print("Caminho mínimo: ", path)
