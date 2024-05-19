import random
import time

# Funkcja generująca graf z cyklem Hamiltona i Eulera
def generate_graph_with_cycles(n, density):
    # Początkowy cykl Hamiltona (każdy wierzchołek połączony w cykl)
    graph = [[0] * n for _ in range(n)]
    hamiltonian_cycle = list(range(n))
    random.shuffle(hamiltonian_cycle)
    
    for i in range(n):
        u = hamiltonian_cycle[i]
        v = hamiltonian_cycle[(i + 1) % n]
        graph[u][v] = 1
        graph[v][u] = 1
    
    # Obliczenie maksymalnej liczby krawędzi
    max_edges = n * (n - 1) // 2
    num_edges = int(density * max_edges)
    
    # Dodawanie dodatkowych krawędzi, aby graf miał odpowiednie nasycenie
    current_edges = set((u, v) for u in range(n) for v in range(u + 1, n))
    edges_to_add = num_edges - (n - 1)  # liczba krawędzi poza cyklem Hamiltona
    while edges_to_add > 0 and current_edges:
        u, v = random.choice(list(current_edges))
        if graph[u][v] == 0:  # jeśli krawędź nie istnieje
            graph[u][v] = graph[v][u] = 1
            edges_to_add -= 1
        current_edges.remove((u, v))
    
    return graph

# Implementacja algorytmu cyklu Eulera bez rekursji
def eulerian_cycle(graph):
    n = len(graph)
    graph_copy = [row[:] for row in graph]  # Tworzymy kopię grafu
    start_vertex = 0
    stack = [start_vertex]
    circuit = []

    while stack:
        v = stack[-1]
        if any(graph_copy[v]):
            u = next(i for i, val in enumerate(graph_copy[v]) if val)
            stack.append(u)
            graph_copy[v][u] = graph_copy[u][v] = 0
        else:
            circuit.append(stack.pop())
    
    return [v + 1 for v in circuit[::-1]]  # Konwersja do 1-indexed

# Implementacja algorytmu cyklu Hamiltona z powracaniem
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
    return [v + 1 for v in backtrack([start_vertex], visited)]  # Konwersja do 1-indexed

# Funkcja do pomiaru czasu dla algorytmu cyklu Eulera
def measure_euler_time(graph_func, graph):
    start_time = time.time()
    graph_func(graph)
    end_time = time.time()
    return end_time - start_time

# Funkcja do pomiaru czasu dla algorytmu cyklu Hamiltona
def measure_hamilton_time(graph_func, graph):
    start_time = time.time()
    graph_func(graph)
    end_time = time.time()
    return end_time - start_time

# Funkcja do wypisania grafu
def print_graph(graph):
    for row in graph:
        print(' '.join(map(str, row)))

# Parametry
n = 22  # liczba wierzchołków
density_30 = 0.3
density_70 = 0.7

# Wygenerowanie grafu z nasyceniem 70%
graph_70 = generate_graph_with_cycles(n, density_70)

# Wypisanie wygenerowanego grafu z nasyceniem 70%
print("Wygenerowany graf z nasyceniem 70%:")
print_graph(graph_70)

# Znalezienie i wypisanie cyklu Eulera oraz pomiar czasu dla grafu z nasyceniem 70%
euler_time_70 = measure_euler_time(eulerian_cycle, graph_70)
euler_cycle_70 = eulerian_cycle(graph_70)
print("\nCykl Eulera dla grafu z nasyceniem 70%:", euler_cycle_70)
print("Czas szukania cyklu Eulera dla grafu z nasyceniem 70%:", euler_time_70, "sekund.")

# Znalezienie i wypisanie cyklu Hamiltona oraz pomiar czasu dla grafu z nasyceniem 70%
hamilton_time_70 = measure_hamilton_time(hamiltonian_cycle, graph_70)
hamilton_cycle_70 = hamiltonian_cycle(graph_70)
print("\nCykl Hamiltona dla grafu z nasyceniem 70%:", hamilton_cycle_70)
print("Czas szukania cyklu Hamiltona dla grafu z nasyceniem 70%:", hamilton_time_70, "sekund.")

print("\n------------------------------------------------------------\n")

# Wygenerowanie grafu z nasyceniem 30%
graph_30 = generate_graph_with_cycles(n, density_30)

# Wypisanie wygenerowanego grafu z nasyceniem 30%
print("Wygenerowany graf z nasyceniem 30%:")
print_graph(graph_30)

# Znalezienie i wypisanie cyklu Eulera oraz pomiar czasu dla grafu z nasyceniem 30%
euler_time_30 = measure_euler_time(eulerian_cycle, graph_30)
euler_cycle_30 = eulerian_cycle(graph_30)
print("\nCykl Eulera dla grafu z nasyceniem 30%:", euler_cycle_30)
print("Czas szukania cyklu Eulera dla grafu z nasyceniem 30%:", euler_time_30, "sekund.")

# Znalezienie i wypisanie cyklu Hamiltona oraz pomiar czasu dla grafu z nasyceniem 30%
hamilton_time_30 = measure_hamilton_time(hamiltonian_cycle, graph_30)
hamilton_cycle_30 = hamiltonian_cycle(graph_30)
print("\nCykl hamilton_cycle_30 dla grafu z nasyceniem 30%:", hamilton_cycle_30)
print("Czas szukania cyklu hamilton_cycle_30 dla grafu z nasyceniem 30%:", hamilton_time_30, "sekund.")