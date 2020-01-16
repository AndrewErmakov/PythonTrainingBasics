def binary_search(list_num: list, number: int) -> int:
    """Выводит индекс значения, которое мы ищем, иначе выводится НИЧТО"""
    low_border = 0
    high_border = len(list_num) - 1

    while low_border <= high_border:

        mid = (low_border + high_border) // 2
        guess = list_num[mid]

        if guess == number:
            return mid

        if guess > number:
            high_border = mid - 1

        else:
            low_border = mid + 1

    return None


def get_answer(number: int) -> str:
    """Вывод положительного ответа, если индекс найден, иначе - ответ отрицательный"""
    if type(number) == int:
        print('YES')
    else:
        print('NO')


# print(binary_search([1, 3, 5, 7, 9], 3))

count_in_list_1, count_in_list_2 = map(int, input().split())

list_numbers_1 = [int(i) for i in input().split()]  # инициализация отсортированного массива
list_numbers_2 = [int(i) for i in input().split()]

for i in range(count_in_list_2):
    get_answer(binary_search(list_numbers_1, list_numbers_2[i]))
