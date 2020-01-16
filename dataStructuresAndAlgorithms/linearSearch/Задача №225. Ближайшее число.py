count_list_elements = int(input())

list_numbers = [int(i) for i in input().split()]

number = int(input())


def search_nearest_number(array_numbers: list, x: int) -> int:
    """Поиск ближайшего элемента к числу x"""

    index_nearest_number = 0
    min_difference = abs(x - array_numbers[index_nearest_number])

    for i in range(1, len(array_numbers)):
        if abs(x - array_numbers[i]) < min_difference:
            index_nearest_number = i
            min_difference = abs(x - array_numbers[index_nearest_number])

    return array_numbers[index_nearest_number]


print(search_nearest_number(list_numbers, number))
