import time
from collections import deque

def eulerian_cycle(graph):
    n = len(graph)
    graph_copy = [row[:] for row in graph]
    stack = [0]
    circuit = deque()

    while stack:
        v = stack[-1]
        found = False
        for u in range(n):
            if graph_copy[v][u]:
                stack.append(u)
                graph_copy[v][u] = 0
                graph_copy[u][v] = 0
                found = True
                break
        if not found:
            circuit.appendleft(stack.pop())

    return [v + 1 for v in circuit]

def hamiltonian_cycle(graph):
    def backtrack(path, visited):
        if len(path) == len(graph) and graph[path[-1]][path[0]] == 1:
            return path + [path[0]]
        for neighbor in range(len(graph[path[-1]])):
            if graph[path[-1]][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                new_path = backtrack(path + [neighbor], visited)
                if new_path:
                    return new_path
                visited.remove(neighbor)
        return None

    start_vertex = 0
    visited = set([start_vertex])
    return [v + 1 for v in backtrack([start_vertex], visited)]

def measure_time(graph_func, graph):
    start_time = time.time()
    result = graph_func(graph)
    end_time = time.time()
    return end_time - start_time, result

def print_cycles(euler_cycle, hamilton_cycle):
    print("Cykl Eulera:", ' '.join(map(str, euler_cycle)))
    print("Cykl Hamiltona:", ' '.join(map(str, hamilton_cycle)))

# Wczytanie danych z pliku
def read_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = [[int(x) for x in line.split()] for line in lines]
    return graph

# Wczytanie grafu z pliku
graph = read_graph("euler.txt")

# Znalezienie cykli
euler_time, euler_cycle = measure_time(eulerian_cycle, graph)
hamilton_time, hamilton_cycle = measure_time(hamiltonian_cycle, graph)

# Wyświetlenie wyników
print_cycles(euler_cycle, hamilton_cycle)
