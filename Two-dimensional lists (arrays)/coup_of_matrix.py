number_lines_list1, number_columns_list1 = map(int, input().split())

numbers_list_1 = []
number_lines_list2, number_columns_list2 = number_columns_list1, number_lines_list1

numbers_list_2 = [[0] * number_columns_list2 for i in range(number_lines_list2)]


for i in range(number_lines_list1):
    row = input().split()

    for j in range(len(row)):
        row[j] = int(row[j])
    numbers_list_1.append(row)

#переворот на 90 градусов
for j in range(number_columns_list1):
    for i in range(number_lines_list1):

        numbers_list_2[j][i] = numbers_list_1[number_lines_list1 - 1 - i][j]

print(number_lines_list2, number_columns_list2)

#вывод результата
for row in numbers_list_2:
    for elem in row:
        print(elem, end=' ')

    print()
