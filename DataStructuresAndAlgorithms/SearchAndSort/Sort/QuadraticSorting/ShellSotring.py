def shell_sorting(nums: list, len_nums: int):
    distance = len_nums // 2

    while distance > 0:
        for i in range(len_nums - distance):
            j = i
            while j >= 0 and nums[j] > nums[j + distance]:
                nums[j], nums[j + distance] = nums[j + distance], nums[j]
                j -= 1

        distance //= 2

    return nums


print(shell_sorting([5, 3, 8, 0, 7, 4, 9, 1, 6, 2], 10))
