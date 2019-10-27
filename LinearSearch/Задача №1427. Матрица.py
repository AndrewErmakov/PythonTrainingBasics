number_lines, number_columns = map(int, input().split())

list_numbers = [['*'] * number_columns for i in range(number_lines)]


def filling_list_numbers(array_numbers: list = list_numbers, num_lines: int = number_lines,
                         num_colmns: int = number_columns):
    """Функция заполнения двумерного списка целыми числами"""
    for i in range(num_lines):
        numbers = input().split()
        for j in range(num_colmns):
            array_numbers[i][j] = int(numbers[j])

    return array_numbers


def determination_saddle_points_of_a_matrix(array_numbers: list = filling_list_numbers(), num_lines: int = number_lines,
                                            num_colmns: int = number_columns):
    """Определение количества седловых точек"""
    count_saddle_points = 0

    for index in range(num_lines * num_colmns):
        elems_in_line = set()
        elems_in_column = set()

        for i_column in range(num_colmns):
            elems_in_line.add(array_numbers[index // num_colmns][i_column])

        for i_line in range(num_lines):
            elems_in_column.add(array_numbers[i_line][index % num_colmns])

        if max(elems_in_column) == min(elems_in_line):
            count_saddle_points += 1

    return count_saddle_points


print(determination_saddle_points_of_a_matrix())
