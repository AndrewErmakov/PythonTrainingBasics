count_list_elements = int(input())

list_numbers = [int(i) for i in input().split()]


def definition_two_min_elem(array_elements: list = list_numbers) -> tuple:
    """Поиск двух самых меньших чисел в спике"""
    # поиск самого меньшего числа
    index_first_smallest_element = 0

    for i in range(1, len(array_elements)):
        if array_elements[index_first_smallest_element] > array_elements[i]:
            index_first_smallest_element = i

    # поиск второго наименьшего числа
    index_second_smallest_element = 0

    for i in range(len(array_elements)):
        if array_elements[i] < array_elements[index_second_smallest_element] and i != index_first_smallest_element:
            index_second_smallest_element = i

    return array_elements[index_first_smallest_element], array_elements[index_second_smallest_element] #почему
    # вернул кортеж?


for elem in definition_two_min_elem():
    print(int(elem), end=' ')
