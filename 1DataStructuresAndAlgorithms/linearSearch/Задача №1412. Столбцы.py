number_for_find = int(input())
size_table = int(input())

list_numbers = [['*'] * size_table for i in range(size_table)]


def filling_list_numbers(array_numbers: list = list_numbers, size: int = size_table):
    """Функция заполнения двумерного списка целыми числами"""
    for i in range(size):
        numbers = input().split()
        for j in range(size):
            array_numbers[i][j] = int(numbers[j])

    return array_numbers


def is_the_column_good(array_numbers: list = filling_list_numbers(), x: int = number_for_find, size: int = size_table):
    """Содержит ли столбец списка число х? (если да, то столбец хороший)"""
    for j in range(size):
        answer = 'NO'
        for i in range(size):
            if array_numbers[i][j] == x:
                answer = "YES"
                break
        print(answer)


is_the_column_good()
