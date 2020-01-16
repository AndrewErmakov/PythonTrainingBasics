number_lines, number_columns = map(int, input().split())
numbers_list = [['*'] * number_columns for i in range(number_lines)]


for i in range(number_lines * number_columns):
    numbers_list[i // number_columns][i % number_columns] = (i // number_columns) * (i % number_columns)


for row in numbers_list:  #вывод двумерного списка
    for elem in row:
        print(elem, end=' ')
    print()
