num_lines, num_columns = map(int, input().split())

numbers_list = [['*'] * num_columns for i in range(num_lines)]


for i in range(num_lines):
    for j in range(num_columns):
        if i == 0 or j == 0:
            numbers_list[i][j] = 1

        else:
            numbers_list[i][j] = numbers_list[i - 1][j] + numbers_list[i][j - 1]


for row in numbers_list:
    for elem in row:
        print(elem, end=' ')
    print()
