y1=int(input())
x1=int(input())
y2=int(input())
x2=int(input())
b=[(1,0), (0, -1), (1, -1), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
if (x2-x1, y2-y1) in b :
    print("YES")
else:
    print("NO")