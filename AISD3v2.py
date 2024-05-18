import random
import time

# Generowanie grafu o n wierzchołkach i danym współczynniku nasycenia
def generate_graph(n, density):
    graph = [[0] * n for _ in range(n)]
    max_edges = n * (n - 1) // 2
    num_edges = int(density * max_edges)
    
    edges = set()
    while len(edges) < num_edges:
        u, v = random.sample(range(n), 2)
        if u > v:
            u, v = v, u
        edges.add((u, v))

    for u, v in edges:
        graph[u][v] = graph[v][u] = 1

    return graph

# Implementacja algorytmu cyklu Eulera bez rekursji
def eulerian_cycle(graph):
    n = len(graph)
    start_vertex = random.randint(0, n - 1)
    stack = [start_vertex]
    circuit = []

    while stack:
        v = stack[-1]
        if any(graph[v]):
            u = next(i for i, val in enumerate(graph[v]) if val)
            stack.append(u)
            graph[v][u] = graph[u][v] = 0
        else:
            circuit.append(stack.pop())
    
    return circuit[::-1]


# Implementacja algorytmu cyklu Hamiltona z powracaniem
def hamiltonian_cycle(graph):
    def backtrack(path, visited):
        if len(path) == len(graph) and path[-1] in graph[path[0]]:
            return path + [path[0]]
        for neighbor in graph[path[-1]]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = backtrack(path + [neighbor], visited)
                if new_path:
                    return new_path
                visited.remove(neighbor)
        return None
    
    start_vertex = random.randint(0, len(graph) - 1)
    visited = set([start_vertex])
    return backtrack([start_vertex], visited)

# Funkcja pomiaru czasu dla algorytmu cyklu Eulera
def measure_euler_time(graph_func, graph):
    start_time = time.time()
    graph_func(graph)
    end_time = time.time()
    return end_time - start_time

# Funkcja pomiaru czasu dla algorytmu cyklu Hamiltona
def measure_hamilton_time(graph_func, graph):
    start_time = time.time()
    graph_func(graph)
    end_time = time.time()
    return end_time - start_time

# Przygotowanie danych pomiarowych
n_values = list(range(5, 1001, 100))
density_30 = 0.3
density_70 = 0.7

euler_times_30 = []
hamilton_times_30 = []
euler_times_70 = []
hamilton_times_70 = []

for n in n_values:
    graph_30 = generate_graph(n, density_30)
    graph_70 = generate_graph(n, density_70)
    
    euler_time_30 = measure_euler_time(eulerian_cycle, graph_30)
    hamilton_time_30 = measure_hamilton_time(hamiltonian_cycle, graph_30)
    euler_times_30.append(euler_time_30)
    hamilton_times_30.append(hamilton_time_30)
    
    euler_time_70 = measure_euler_time(eulerian_cycle, graph_70)
    hamilton_time_70 = measure_hamilton_time(hamiltonian_cycle, graph_70)
    euler_times_70.append(euler_time_70)
    hamilton_times_70.append(hamilton_time_70)

# Wyświetlenie wyników
print("Czasy wykonania dla grafu o 30% nasycenia:")
print("Algorytm cyklu Eulera:", euler_times_30)
print("Algorytm cyklu Hamiltona:", hamilton_times_30)

print("\nCzasy wykonania dla grafu o 70% nasycenia:")
print("Algorytm cyklu Eulera:", euler_times_70)
print("Algorytm cyklu Hamiltona:", hamilton_times_70)
