number_lines, number_columns = map(int, input().split())

numbers_list = [[0] * number_columns for i in range(number_lines)]

count_mines = int(input())
coordinate_mine_x = coordinate_mine_y = 0

for mine in range(count_mines):  # располагаем мины
    coordinate_mine_x, coordinate_mine_y = map(int, input().split())

    for i in range(number_lines):
        for j in range(number_columns):
            if coordinate_mine_x - 1 == i and coordinate_mine_y - 1 == j:
                numbers_list[i][j] = '*'

for i in range(number_lines):
    for j in range(number_columns):
        if numbers_list[i][j] != '*':

            while i - 1 >= 0:
                if numbers_list[i - 1][j] == '*':
                    numbers_list[i][j] += 1
                break
            while i - 1 >= 0 and j - 1 >= 0:
                if numbers_list[i - 1][j - 1] == '*':
                    numbers_list[i][j] += 1
                break
            while i - 1 >= 0 and j + 1 < number_columns:
                if numbers_list[i - 1][j + 1] == '*':
                    numbers_list[i][j] += 1
                break

            while i + 1 < number_lines:
                if numbers_list[i + 1][j] == '*':
                    numbers_list[i][j] += 1
                break

            #1
            while i + 1 < number_lines and j - 1 >= 0:
                if numbers_list[i + 1][j - 1] == '*':
                    numbers_list[i][j] += 1
                break

            while i + 1 < number_lines and j + 1 < number_columns:
                if numbers_list[i + 1][j + 1] == '*':
                    numbers_list[i][j] += 1
                break

            while j - 1 >= 0:
                if numbers_list[i][j - 1] == '*':
                    numbers_list[i][j] += 1
                break

            while j + 1 < number_columns:
                if numbers_list[i][j + 1] == '*':
                    numbers_list[i][j] += 1
                break

for row in numbers_list:  # вывод двумерного списка
    for elem in row:
        print(elem, end=' ')
    print()
