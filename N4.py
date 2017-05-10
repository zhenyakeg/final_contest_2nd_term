s = [int(x) for x in input().split()]
A=[]
B=[]
for i in range(len(s)):
    if s[i]%2==0:
        A.append(s[i])
    elif s[i]%2==1:
        B.append(s[i])
l=sorted(A) + sorted(B)
print(*l)