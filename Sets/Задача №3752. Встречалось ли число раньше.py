list_numbers = [int(i) for i in input().split()]

set_numbers = set()

for i in range(len(list_numbers)):
    if list_numbers[i] in set_numbers:
        print('YES')
    else:
        print('NO')
        set_numbers.add(list_numbers[i])

