num_lines, num_columns = map(int, input().split())

numbers_list = [['*'] * num_columns for i in range(num_lines)]

current_number = 0

for i in range(num_lines):
    for j in range(num_columns):

        if i % 2 == 0:
            numbers_list[i][j] = current_number

        if i % 2 == 1:
            numbers_list[i][num_columns - 1 - j] = current_number

        current_number += 1

for row in numbers_list:
    for elem in row:
        print(elem, end=' ')

    print()
