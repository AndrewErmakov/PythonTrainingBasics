def sort_selection_by_max(nums: list, count_nums: int):
    for i in range(count_nums - 1, 0, -1):
        index_max_elem = i

        for j in range(i - 1, 0, -1):
            if nums[j] > nums[index_max_elem]:
                index_max_elem = j

        nums[index_max_elem], nums[i] = nums[i], nums[index_max_elem]


# count_numbers = int(input())
# list_numbers = list(map(int, input().split()))
#
# for elem in sort_selection_by_max(list_numbers, count_numbers):

# for i in range()