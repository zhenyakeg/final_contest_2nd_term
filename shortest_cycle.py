m = int(input())
graph = {}
for j in range(m):
    v1, v2 = input().split()
    graph[v1] = graph.get(v1, []) + [v2]


def shortest_cycle(graph):
    min_time = float('inf')
    resulting_path = []
    for start in graph:
        used = set()
        path = {}
        Q = []
        used.add(start)
        Q.append((start, 0))
        path[start] = [start]
        while Q:
            vertex, time = Q.pop(0)
            time += 1
            if time >= min_time:
                break
            for neighbour in graph.get(vertex, []):
                if neighbour not in used:
                    Q.append((neighbour, time))
                    used.add(vertex)
                    path[neighbour] = path[vertex] + [neighbour]
                elif neighbour == start:
                    min_time = time
                    resulting_path = path[vertex] + [start]
                    break
            path.pop(vertex)
        path[start] = []
    return resulting_path

res = shortest_cycle(graph)
if res:
    print(' '. join(map(str, res)))
else:
    print(-1)