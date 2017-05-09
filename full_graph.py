n, m = tuple(map(int, input().split()))
graph = [[] for i in range(n)]
for j in range(m):
    vert1, vert2 = tuple(map(lambda x: int(x)-1, input().split()))
    graph[vert1].append(vert2)
    graph[vert2].append(vert1)
def check_fullness(graph):
    for vertex in range(len(graph)):
        for neighbour in range(len(graph)):
            if neighbour != vertex and neighbour not in graph[vertex]:
                return False
    return True
if check_fullness(graph):
    print('YES')
else:
    print('NO')
