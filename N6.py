import sys
n=int(input())
A=[[0]*n for i in range(n)]
for i in range(n):
    A[i]=[int(x) for x in input().split()]
for i in range(n):
    for j in range(n):
        if A[i][j]!= A[j][i]:
            print('NO')
            sys.exit(0)
print('YES')