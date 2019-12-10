from pprint import pprint


def create_list_members(count_members: int):
    list_results_members = []
    for i in range(count_members):
        result_each_member = [int(i) for i in input().split()]
        list_results_members.append(result_each_member)

    return list_results_members


def bubble_sort(nums: list, count_nums: int):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, count_nums):
            if nums[i - 1][1] < nums[i][1]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapped = True

            if nums[i - 1][1] == nums[i][1] and nums[i - 1][0] > nums[i][0]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapped = True

    return nums


count_participants = int(input())
list_results = bubble_sort(create_list_members(count_participants), count_participants)
for j in range(count_participants):
    for elem in list_results[j]:
        print(elem, end=' ')
    print()
