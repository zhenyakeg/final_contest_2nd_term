n = int(input())
seq = list(map(int, input().split()))
def find_symmetrical_part(seq, start = 0):
    i = 0
    while i < len(seq)//2 and seq[i] == seq[len(seq) - i -1]:
        i+=1
    if i == len(seq)//2:
        return start
    else:
        return find_symmetrical_part(seq[1::], start + 1)


start_of_symmetry = find_symmetrical_part(seq)
additional_part = seq[0 : start_of_symmetry][::-1]
print(len(additional_part))
print(' '.join(map(str, additional_part)))
