def merge(left_part: list, right_part: list):
    result_sorted_list = []
    left_list_index = right_list_index = 0

    len_left_part, len_right_part = len(left_part), len(right_part)

    for _ in range(len_left_part + len_right_part):

        if left_list_index < len_left_part and right_list_index < len_right_part:

            if left_part[left_list_index] <= right_part[right_list_index]:
                result_sorted_list.append(left_part[left_list_index])
                left_list_index += 1

            else:
                result_sorted_list.append(right_part[right_list_index])
                right_list_index += 1

        elif left_list_index == len_left_part:
            result_sorted_list.append(right_part[right_list_index])
            right_list_index += 1

        elif right_list_index == len_right_part:
            result_sorted_list.append(left_part[left_list_index])
            left_list_index += 1

    return result_sorted_list


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    mid_index = len(nums) // 2

    left_list = merge_sort(nums[:mid_index])
    right_list = merge_sort(nums[mid_index:])

    return merge(left_list, right_list)


count_nums = int(input())
list_nums = [int(i) for i in input().split()]
for elem in merge_sort(list_nums):
    print(elem, end=' ')

