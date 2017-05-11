n = int(input())
pascal = [[1], [1, 1]] + [[0 for j in range(i + 1)] for i in range(2, n+1)]
for i in range(2, n + 1):
    pascal[i][0] = 1
    pascal[i][i] = 1
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
for line in pascal:
    print(' '.join(map(str, line)))
