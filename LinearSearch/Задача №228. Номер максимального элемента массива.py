count_list_elements = int(input())

list_numbers = [int(i) for i in input().split()]


def find_index_max_elem(array_elements: list) -> int:
    index_max_elem = 0
    for i in range(1, len(array_elements)):
        if array_elements[i] > array_elements[index_max_elem]:
            index_max_elem = i

    return index_max_elem + 1


print(find_index_max_elem(list_numbers))
