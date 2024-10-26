import networkx as nx
import matplotlib.pyplot as plt
from task3.graph import Graph
from task3.minHeap import MinHeap


def dijkstra(graph, src):
    V = graph.V
    dist = [float('inf')] * V
    dist[src] = 0
    min_heap = MinHeap()
    predecessors = [-1] * V
    for v in range(V):
        min_heap.insert(v, dist[v])
    while not min_heap.is_empty():
        min_node = min_heap.extract_min()
        u = min_node[1]
        for neighbor, weight in graph.graph[u]:
            if dist[u] + weight < dist[neighbor]:
                dist[neighbor] = dist[u] + weight
                predecessors[neighbor] = u
                min_heap.decrease_key(neighbor, dist[neighbor])
    return dist, predecessors


def get_path(predecessors, target):
    path = []
    while target != -1:
        path.append(target)
        target = predecessors[target]
    return path[::-1]


g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

distances, predecessors = dijkstra(g, 0)
for i, distance in enumerate(distances):
    path = get_path(predecessors, i)
    print(f"Відстань від вершини 0 до вершини {i}: {distance}, шлях: {path}")
