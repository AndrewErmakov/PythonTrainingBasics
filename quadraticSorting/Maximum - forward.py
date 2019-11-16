def search_max_elem(nums: list, count: int):
    index_max_elem = 0

    for i in range(count):
        if nums[i] > nums[index_max_elem]:
            index_max_elem = i

    return index_max_elem


count_elements = int(input())

numbers_list = [int(i) for i in input().split()]

index_max_element = search_max_elem(numbers_list, count_elements)

numbers_list[0], numbers_list[index_max_element] = numbers_list[index_max_element], numbers_list[0]

for elem in numbers_list:
    print(elem, end=' ')


