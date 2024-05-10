# Алгоритм Дейкстры

def dijkstra(graph, start):
    
    # Создаем словарь для хранения кратчайших расстояний от начальной до всех остальных вершин
    shortest_distances = {vertex: float('infinity') for vertex in graph}
    shortest_distances[start] = 0

    # Создаем множество для отслеживания вершин, для которых уже найден кратчайший путь
    visited = set()

    # Пока есть непосещенные вершины
    while len(visited) != len(graph):
        # Выбираем вершину с наименьшим кратчайшим расстоянием
        current_vertex = min((set(shortest_distances.keys()) - visited), key=shortest_distances.get)

        # Помечаем текущую вершину как посещенную
        visited.add(current_vertex)

        # Обновляем расстояния до соседних вершин
        for neighbour, distance in graph[current_vertex].items():
            if neighbour not in visited:
                new_distance = shortest_distances[current_vertex] + distance
                if new_distance < shortest_distances[neighbour]:
                    shortest_distances[neighbour] = new_distance

    return shortest_distances

# Пример
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'A': 1, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 1},
    'D': {'B': 4, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print("Кратчайшие расстояния от вершины", start_vertex, "до всех остальных:")
for vertex, distance in distances.items():
    print("До вершины {}: {}".format(vertex, distance))