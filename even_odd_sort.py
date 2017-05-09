def even_odd_sort(input_list):
    even_list, odd_list = [], []
    for number in input_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    return sorted(odd_list) + sorted(even_list, reverse= True)

n = int(input())
input_list = list(map(int, input().split()))
print(' '. join(map(str, even_odd_sort(input_list))))