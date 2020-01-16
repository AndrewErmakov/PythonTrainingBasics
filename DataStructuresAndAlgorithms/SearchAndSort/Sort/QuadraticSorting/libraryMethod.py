# Задача №1436. Библиотечный метод
# https://www.informatics.mccme.ru/mod/statements/view3.php?id=271&chapterid=1436#1


def insertion_sort(list_nums: list, count_nums: int):
    for i in range(1, count_nums):

        x = list_nums[i]
        index_prev_item_from_x = i - 1
        swapped = None

        while x < list_nums[index_prev_item_from_x] and index_prev_item_from_x >= 0:
            list_nums[index_prev_item_from_x + 1] = list_nums[index_prev_item_from_x]
            index_prev_item_from_x -= 1
            swapped = True

        list_nums[index_prev_item_from_x + 1] = x

        if swapped is not None:
            print_list(list_nums)
    # return list_nums


def print_list(nums_list):
    for elem in nums_list:
        print(elem, end=' ')
    print()


count_elements = int(input())
list_numbers = [int(i) for i in input().split()]
insertion_sort(list_numbers, count_elements)
