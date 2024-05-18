import random
import time

def generate_eulerian_hamiltonian_graph(n, edge_density):
    graph = {i: [(i + 1) % n] for i in range(n)}
    for i in range(n):
        graph[(i + 1) % n].append(i)

    max_possible_edges = (n * (n - 1)) // 2
    target_edges = int(max_possible_edges * edge_density)
    current_edges = sum(len(neighbors) for neighbors in graph.values())
    remaining_edges = target_edges - current_edges

    while remaining_edges > 0:
        u, v = random.sample(range(n), 2)
        if v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)
            remaining_edges -= 1

    return graph

def eulerian_cycle(graph, start_vertex):
    cycle = []

    def euler(v):
        while graph[v]:
            w = graph[v].pop()
            graph[w].remove(v)
            euler(w)
        cycle.append(v)

    euler(start_vertex)
    return cycle[::-1]

def has_eulerian_cycle(graph):
    return all(len(neighbors) % 2 == 0 for neighbors in graph.values())

def hamiltonian_cycle(graph, start_vertex):
    n = len(graph)
    path = []

    def hamilton(v):
        path.append(v)
        if len(path) == n:
            if path[0] in graph[path[-1]]:
                return True
            else:
                path.pop()
                return False
        for neighbor in graph[v]:
            if neighbor not in path:
                if hamilton(neighbor):
                    return True
        path.pop()
        return False

    for start in range(n):
        if hamilton(start):
            return True
    return False

def measure_algorithm_time(graph, algorithm_func, start_vertex):
    start_time = time.time()
    algorithm_func(graph, start_vertex)
    end_time = time.time()
    return end_time - start_time

# Przygotowanie punktów pomiarowych
n_values = list(range(5, 51, 3))  # liczba wierzchołków
edge_density_sparse = 0.3  # współczynnik nasycenia dla grafu rzadkiego
edge_density_dense = 0.7   # współczynnik nasycenia dla grafu gęstego
iterations = 15  # liczba iteracji dla każdej wartości n

# Pomiar czasu dla grafu rzadkiego
for n in n_values:
    graph = generate_eulerian_hamiltonian_graph(n, edge_density_sparse)
    avg_time_A = 0
    avg_time_B = 0

    for _ in range(iterations):
        time_A = measure_algorithm_time(graph, eulerian_cycle, 0)
        time_B = measure_algorithm_time(graph, hamiltonian_cycle, 0)
        avg_time_A += time_A
        avg_time_B += time_B

    avg_time_A /= iterations
    avg_time_B /= iterations

    print(f"Graph with {n} vertices and 30% density - Eulerian Cycle: {avg_time_A} seconds, Hamiltonian Cycle: {avg_time_B} seconds")
    print("Graph properties - Eulerian:", has_eulerian_cycle(graph), ", Hamiltonian:", hamiltonian_cycle(graph, 0))

# Pomiar czasu dla grafu gęstego
for n in n_values:
    graph = generate_eulerian_hamiltonian_graph(n, edge_density_dense)
    avg_time_A = 0
    avg_time_B = 0

    for _ in range(iterations):
        time_A = measure_algorithm_time(graph, eulerian_cycle, 0)
        time_B = measure_algorithm_time(graph, hamiltonian_cycle, 0)
        avg_time_A += time_A
        avg_time_B += time_B

    avg_time_A /= iterations
    avg_time_B /= iterations

    print(f"Graph with {n} vertices and 70% density - Eulerian Cycle: {avg_time_A} seconds, Hamiltonian Cycle: {avg_time_B} seconds")
    print("Graph properties - Eulerian:", has_eulerian_cycle(graph), ", Hamiltonian:", hamiltonian_cycle(graph, 0))
