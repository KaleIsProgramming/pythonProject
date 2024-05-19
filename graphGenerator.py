import random

# Funkcja generująca graf z cyklem Hamiltona i Eulera
def generate_graph_with_cycles(n):
    # Początkowy cykl Hamiltona (każdy wierzchołek połączony w cykl)
    graph = [[0] * n for _ in range(n)]
    hamiltonian_cycle = list(range(n))
    random.shuffle(hamiltonian_cycle)
    
    for i in range(n):
        u = hamiltonian_cycle[i]
        v = hamiltonian_cycle[(i + 1) % n]
        graph[u][v] = 1
        graph[v][u] = 1
    
    # Dodawanie dodatkowych krawędzi, aby każdy wierzchołek miał parzysty stopień
    for i in range(n):
        if sum(graph[i]) % 2 != 0:
            for j in range(i + 1, n):
                if sum(graph[j]) % 2 != 0:
                    graph[i][j] = 1
                    graph[j][i] = 1
                    break
    
    return graph

# Funkcja do wypisania grafu
def print_graph(graph):
    for row in graph:
        print(' '.join(map(str, row)))

# Funkcja do zapisania grafu do pliku
def save_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        for row in graph:
            file.write(' '.join(map(str, row)) + '\n')

# Parametry
n = 66  # liczba wierzchołków

# Generowanie grafu z cyklami
graph = generate_graph_with_cycles(n)

# Wypisanie wygenerowanego grafu
print("Wygenerowany graf:")
print_graph(graph)

# Zapisanie grafu do pliku
filename = 'euler.txt'
save_graph_to_file(graph, filename)
print(f"\nGraf został zapisany do pliku {filename}")
