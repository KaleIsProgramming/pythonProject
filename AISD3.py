import random

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

n = 6  # liczba wierzchołków
edge_density_sparse = 0.3  # współczynnik nasycenia dla grafu rzadkiego
edge_density_dense = 0.7   # współczynnik nasycenia dla grafu gęstego

graph1 = generate_eulerian_hamiltonian_graph(n, edge_density_sparse)

graph2 = generate_eulerian_hamiltonian_graph(n, edge_density_dense)

print("Graph 1 adjacency list:", graph1)
if has_eulerian_cycle(graph1):
    cycle1 = eulerian_cycle({k: v.copy() for k, v in graph1.items()}, 0)
    print("Eulerian Cycle for Graph 1:", cycle1)
else:
    print("Graph 1 does not have an Eulerian Cycle")

if hamiltonian_cycle(graph1, 0):
    print("Graph 1 has a Hamiltonian Cycle")
else:
    print("Graph 1 does not have a Hamiltonian Cycle")

print("Graph 2 adjacency list:", graph2)
if has_eulerian_cycle(graph2):
    cycle2 = eulerian_cycle({k: v.copy() for k, v in graph2.items()}, 0)
    print("Eulerian Cycle for Graph 2:", cycle2)
else:
    print("Graph 2 does not have an Eulerian Cycle")

if hamiltonian_cycle(graph2, 0):
    print("Graph 2 has a Hamiltonian Cycle")
else:
    print("Graph 2 does not have a Hamiltonian Cycle")