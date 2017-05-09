n = int(input())
experiment = list(map(int, input().split()))
cash = [0] * (n+1)
for i in range(1, len(experiment) + 1):
    if experiment[i-1] == 5:
        cash[i] = cash[i-1] + 1
    else:
        cash[i] = cash[i-1] - experiment[i-1]//5 + 1
initial_money = min(cash)
if initial_money <= 0:
    print(-initial_money)
else:
    print(0)


