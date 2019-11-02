def leftside_binary_search(list_num: list, key: int) -> tuple:
    """Реализация левостороннего двоичного поиска"""
    left_border = -1
    right_border = len(list_num)

    while right_border - left_border > 1:

        mid = (left_border + right_border) // 2

        if list_num[mid] < key:
            left_border = mid

        else:
            right_border = mid

    return left_border, right_border


def rightside_binary_search(list_num: list, key: int) -> tuple:
    """Реализация правостороннего двоичного поиска"""
    left_border = -1
    right_border = len(list_num)

    while right_border - left_border > 1:

        mid = (left_border + right_border) // 2

        if list_num[mid] <= key:
            left_border = mid

        else:
            right_border = mid

    return left_border, right_border


count_in_list_1, count_in_list_2 = map(int, input().split())

list_numbers_1 = [int(i) for i in input().split()]  # инициализация отсортированного массива
list_numbers_2 = [int(i) for i in input().split()]

for i in range(count_in_list_2):
    left_border_1 = leftside_binary_search(list_numbers_1, list_numbers_2[i])[0]
    right_border_1 = leftside_binary_search(list_numbers_1, list_numbers_2[i])[1]

    left_border_2 = rightside_binary_search(list_numbers_1, list_numbers_2[i])[0]
    right_border_2 = rightside_binary_search(list_numbers_1, list_numbers_2[i])[1]

    if left_border_1 == left_border_2 and right_border_1 == right_border_2:  # если число, которое нужно найти, отсутствует
        print(0)

    else:
        print(right_border_1 + 1, left_border_2 + 1)

