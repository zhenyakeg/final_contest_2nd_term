n, m = map(int, input().split())
graph = {(i, j): {} for i in range(n) for j in [0, 1]}
for j in range(m):
    v1, v2, c = map(int, input().split())
    graph[(v1, 0)][v2, 1] = c
    graph[(v1, 1)][(v2, 0)] = c
    graph[(v2, 0)][(v1, 1)] = c
    graph[(v2, 1)][(v1, 0)] = c
k = int(input())
tasks = []
for t in range(k):
    v1, v2 = map(int, input().split())
    tasks.append(((v1, 0), (v2, 0)))

def dijkstra(graph, start, finish):
    distances = {v: float('inf') for v in graph}
    ways = {v: [] for v in graph}
    used = set()
    distances[start] = 0
    ways[start] = [start]
    Q = [start]
    for i in range(len(graph)):
        min_d = float('inf')
        for vertex in distances:
            if distances[vertex] < min_d and vertex not in used:
                min_d = distances[vertex]
                current_node = vertex

        for neighbour in graph[current_node]:
            l = distances[current_node] + graph[current_node][neighbour]
            if l < distances[neighbour]:
                distances[neighbour] = l
                ways[neighbour] = ways[current_node] + [neighbour]
        used.add(current_node)
    return distances[finish], ways[finish]

for task in tasks:
    res = dijkstra(graph, task[0], task[1])[1]
    if len(res) == 0:
        print(-1)
    else:
        print(' '.join(map(lambda x: str(x[0]), res)))


