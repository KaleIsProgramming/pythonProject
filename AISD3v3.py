import random
import time

# Generowanie eulerowskiego grafu nieskierowanego o 50% nasyceniu krawędziami
def generate_euler_graph(n):
    graph = [[0] * n for _ in range(n)]
    max_edges = n * (n - 1) // 2
    num_edges = max_edges // 2  # 50% nasycenie krawędziami

    edges = set()
    while len(edges) < num_edges:
        u, v = random.sample(range(n), 2)
        if u > v:
            u, v = v, u
        edges.add((u, v))

    for u, v in edges:
        graph[u][v] = graph[v][u] = 1

    return graph

# Implementacja algorytmu przeszukiwania wszerz (BFS) dla znajdowania cyklu Hamiltona
def find_hamilton_cycles(graph):
    def bfs(vertex, path, visited):
        if len(path) == len(graph) and path[-1] in graph[path[0]]:
            cycles.append(path + [path[0]])
            return
        for neighbor, connected in enumerate(graph[vertex]):
            if connected and neighbor not in visited:
                visited.add(neighbor)
                bfs(neighbor, path + [neighbor], visited)
                visited.remove(neighbor)

    cycles = []
    for start_vertex in range(len(graph)):
        bfs(start_vertex, [start_vertex], set([start_vertex]))
    return cycles

# Funkcja pomiaru czasu dla znajdowania cykli Hamiltona
def measure_hamilton_time(graph):
    start_time = time.time()
    find_hamilton_cycles(graph)
    end_time = time.time()
    return end_time - start_time

# Przygotowanie danych pomiarowych
n_values = list(range(5, 101, 5))
hamilton_times = []

for n in n_values:
    graph = generate_euler_graph(n)
    hamilton_time = measure_hamilton_time(graph)
    hamilton_times.append(hamilton_time)

# Wyświetlenie wyników
print("Czasy wykonania dla eulerowskiego grafu o 50% nasycenia:")
print("Algorytm cyklu Hamiltona:", hamilton_times)
