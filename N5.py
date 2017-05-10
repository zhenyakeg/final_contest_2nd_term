N=int(input())
s=list(map(int, input().split()))
n=float('+inf')
for i in range(len(s)):
    if s[i] < 0:
        for j in range(i+1, len(s)):
            if s[i]== -s[j]:
                n=min(n, abs(i-j))
if n == float('inf'):
    print(0)
else:
    print(n)