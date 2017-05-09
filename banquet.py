n, m = tuple(map(int, input().split()))
graph = [[] for i in range(n)]
for j in range(m):
    vip1, vip2 = tuple(map(lambda x: int(x) - 1, input().split()))
    graph[vip1].append(vip2)
    graph[vip2].append(vip1)

def check_duality(graph, start = 0):
    used = set()
    used.add(start)
    parts = [0] * n
    Q = []
    Q.append(start)
    while Q:
        vertex = Q.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in used:
                used.add(neighbour)
                Q.append(neighbour)
                parts[neighbour] = (parts[vertex]+1) % 2
            else:
                if parts[vertex] == parts[neighbour]:
                    return False, parts
    return True, parts


result = check_duality(graph)

if result[0]:
    print('YES')
    first_part = [i+1 for i in range(n) if result[1][i] == 0]
    print(' '.join(list(map(str, first_part))))
else:
    print('NO')