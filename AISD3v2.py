import random
import time
from collections import deque, defaultdict

def generate_graph_with_cycles(n, density):
    graph = [[0] * n for _ in range(n)]
    hamiltonian_cycle = list(range(n))
    random.shuffle(hamiltonian_cycle)
    
    for i in range(n):
        u = hamiltonian_cycle[i]
        v = hamiltonian_cycle[(i + 1) % n]
        graph[u][v] = 1
        graph[v][u] = 1
    
    max_edges = n * (n - 1) // 2
    num_edges = int(density * max_edges)
    edges_to_add = num_edges - n

    while edges_to_add > 0:
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        if u != v and graph[u][v] == 0:
            graph[u][v] = graph[v][u] = 1
            edges_to_add -= 1
    
    return graph

def eulerian_cycle(graph):
    n = len(graph)
    graph_copy = [row[:] for row in graph]  # Tworzymy kopię grafu
    stack = [0]  # Stos do zarządzania wierzchołkami
    circuit = deque()  # Lista do przechowywania cyklu Eulera

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

def print_graph(graph):
    for row in graph:
        print(' '.join(map(str, row)))

n = 212
density_30 = 0.3
density_70 = 0.7

graph_70 = generate_graph_with_cycles(n, density_70)
print("Wygenerowany graf z nasyceniem 70%:")
#print_graph(graph_70)

euler_time_70, euler_cycle_70 = measure_time(eulerian_cycle, graph_70)
print("\nCykl Eulera dla grafu z nasyceniem 70%:", euler_cycle_70)
print("Czas szukania cyklu Eulera dla grafu z nasyceniem 70%:", euler_time_70, "sekund.")

hamilton_time_70, hamilton_cycle_70 = measure_time(hamiltonian_cycle, graph_70)
print("\nCykl Hamiltona dla grafu z nasyceniem 70%:", hamilton_cycle_70)
print("Czas szukania cyklu Hamiltona dla grafu z nasyceniem 70%:", hamilton_time_70, "sekund.")

print("\n------------------------------------------------------------\n")

graph_30 = generate_graph_with_cycles(n, density_30)
print("Wygenerowany graf z nasyceniem 30%:")
#print_graph(graph_30)

euler_time_30, euler_cycle_30 = measure_time(eulerian_cycle, graph_30)
print("\nCykl Eulera dla grafu z nasyceniem 30%:", euler_cycle_30)
print("Czas szukania cyklu Eulera dla grafu z nasyceniem 30%:", euler_time_30, "sekund.")

hamilton_time_30, hamilton_cycle_30 = measure_time(hamiltonian_cycle, graph_30)
print("\nCykl Hamiltona dla grafu z nasyceniem 30%:", hamilton_cycle_30)
print("Czas szukania cyklu Hamiltona dla grafu z nasyceniem 30%:", hamilton_time_30, "sekund.")
