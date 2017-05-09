N = int(input())

def list_factorials(n):
    factorials = [1, 1]
    i = 1
    while factorials[i] < n:
        i += 1
        factorials.append(factorials[i-1]*i)
    if factorials[-1] > n:
        return factorials[1:-1:]
    else:
        return factorials[1::]
print(' '. join(map(str, list_factorials(N))))
