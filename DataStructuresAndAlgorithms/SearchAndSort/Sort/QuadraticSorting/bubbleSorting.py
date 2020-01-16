def bubble_sort(nums: list, count_nums: int):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, count_nums):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]

                swapped = True

    return nums


count_numbers = int(input())
list_numbers = [int(i) for i in input().split()]

for elem in bubble_sort(list_numbers, count_numbers):
    print(elem, end=' ')


