import random

def generate_euler_graph(n):
    graph = [[0] * n for _ in range(n)]
    
    for i in range(n - 1):
        graph[i][i + 1] = graph[i + 1][i] = 1
    graph[n - 1][0] = graph[0][n - 1] = 1
    
    edges_to_add = (n * (n - 1) // 2) // 2
    while edges_to_add > 0:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v and graph[u][v] == 0:
            graph[u][v] = graph[v][u] = 1
            edges_to_add -= 1
    
    return graph

def is_valid_move(v, graph, path, pos):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True

def hamiltonian_cycles(graph):
    n = len(graph)
    cycles = []

    def dfs(vertex, path):
        if len(path) == n:
            if graph[path[-1]][path[0]] == 1:
                cycles.append(path[:])  # Dodanie cyklu Hamiltona
            return
        for neighbor in range(n):
            if is_valid_move(neighbor, graph, path, len(path)):
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

    for start_vertex in range(n):
        dfs(start_vertex, [start_vertex])

    return cycles

euler_graph = generate_euler_graph(10)

cycles = hamiltonian_cycles(euler_graph)

# Wypisanie eulerowskiego grafu i znalezionych cykli Hamiltona
print("Wygenerowany eulerowski graf nieskierowany z nasyceniem 50%:")
for row in euler_graph:
    print(" ".join(map(str, row)))

print("\nWszystkie cykle Hamiltona w grafie:")
if cycles:
    for cycle in cycles:
        print(cycle)
else:
    print("Brak cykli Hamiltona w grafie.")
