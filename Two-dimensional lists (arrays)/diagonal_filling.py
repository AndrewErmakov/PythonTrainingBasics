num_lines, num_columns = map(int, input().split())

numbers_list = [['*'] * num_columns for i in range(num_lines)]

current_number = 0

for i in range(num_lines):
    for j in range(num_columns):
        if numbers_list[i][j] == '*':
            index = 0
            while i + index < num_lines and j - index >= 0:
                numbers_list[i + index][j - index] = current_number
                index += 1

                current_number += 1

for row in numbers_list:
    for elem in row:
        print(elem, end=' ')

    print()
