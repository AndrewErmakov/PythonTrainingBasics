def insertion_sort(list_nums: list, count_nums: int):
    for i in range(1, count_nums):

        x = list_nums[i]
        index_prev_item_from_x = i - 1

        while x < list_nums[index_prev_item_from_x] and index_prev_item_from_x >= 0:
            list_nums[index_prev_item_from_x + 1] = list_nums[index_prev_item_from_x]
            index_prev_item_from_x -= 1

        list_nums[index_prev_item_from_x + 1] = x

    return list_nums


len_list = int(input())
list_numbers = [int(i) for i in input().split()]

for elem in insertion_sort(list_numbers, len_list):
    print(elem, end=' ')


