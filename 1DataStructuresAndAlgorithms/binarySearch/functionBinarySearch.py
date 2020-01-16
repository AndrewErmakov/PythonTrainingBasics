def binary_search(list_num: list, number: int) -> int:
    """Выводит индекс значения, которое мы ищем, иначе выводится НЕ НАЙДЕНО"""
    low_border = 0
    high_border = len(list_num) - 1

    while low_border <= high_border:

        mid = low_border + (high_border - low_border) // 2
        guess = list_num[mid]

        if guess == number:
            return mid

        if guess > number:
            high_border = mid - 1

        else:
            low_border = mid + 1

    return None


print(binary_search([1, 3, 5, 7, 9], 3))
