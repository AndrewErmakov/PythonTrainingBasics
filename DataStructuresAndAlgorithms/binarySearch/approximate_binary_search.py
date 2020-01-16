def binary_search(list_num: list, number: int) -> int:
    """Выводит индекс значения, которое мы ищем или индекс ближайшего значения"""
    low_border = 0
    high_border = len(list_num) - 1

    min_difference = list_num[-1] - list_num[0] + 1
    nearest_element_index = None  # индекс числа, наиболее близкое к данному

    while low_border <= high_border:

        mid = (low_border + high_border) // 2
        guess = list_num[mid]

        if guess == number:
            return guess

        if nearest_element_index is None:

            min_difference = abs(guess - number)
            nearest_element_index = mid

        else:
            if abs(guess - number) < min_difference or (
                    abs(guess - number) == min_difference and guess < list_num[nearest_element_index]):
                min_difference = abs(guess - number)
                nearest_element_index = mid

        if guess > number:
            high_border = mid - 1

        if guess < number:
            low_border = mid + 1

    return list_num[nearest_element_index]


count_in_list_1, count_in_list_2 = map(int, input().split())

list_numbers_1 = [int(i) for i in input().split()]  # инициализация отсортированного массива
list_numbers_2 = [int(i) for i in input().split()]

for i in range(count_in_list_2):
    print(binary_search(list_numbers_1, list_numbers_2[i]))

