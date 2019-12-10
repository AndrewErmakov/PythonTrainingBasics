# Задача №1418. Разные
# https://www.informatics.mccme.ru/mod/statements/view3.php?id=1129&chapterid=1418#1

count_elements = int(input())
list_elements = [int(i) for i in input().split()]


def quick_sort(nums: list):
    # count_different_elements = 0
    if len(nums) <= 1:
        return nums

    else:
        medial_element = nums[len(nums) // 2]

    s_nums = [num for num in nums if num < medial_element]
    e_nums = [medial_element] * nums.count(medial_element)

    b_nums = [num for num in nums if num > medial_element]

    return quick_sort(s_nums) + e_nums + quick_sort(b_nums)


def find_count_different_elements(sorted_list: list, count_nums):
    count_different_elements = 1
    for i in range(1, count_nums):
        if sorted_list[i - 1] != sorted_list[i]:
            count_different_elements += 1

    return count_different_elements


def make_set_from_list(nums: list):
    return len(set(nums))


number_different_elements_1 = find_count_different_elements(quick_sort(list_elements), count_elements)
number_different_elements_2 = make_set_from_list(list_elements)
print(number_different_elements_1, number_different_elements_2)
