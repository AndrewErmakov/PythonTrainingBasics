def sort_selection_by_min(nums: list, count_nums: int):
    for i in range(count_nums):

        index_lowest_value = i

        for j in range(i + 1, count_nums):
            if nums[j] < nums[index_lowest_value]:
                index_lowest_value = j

        nums[i], nums[index_lowest_value] = nums[index_lowest_value], nums[i]

    return nums


count_numbers = int(input())
list_numbers = list(map(int, input().split()))

for elem in sort_selection_by_min(list_numbers, count_numbers):
    print(elem, end=' ')
