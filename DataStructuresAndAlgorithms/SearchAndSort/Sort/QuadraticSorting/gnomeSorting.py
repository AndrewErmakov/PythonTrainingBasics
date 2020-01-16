def gnome_sort(nums: list) -> list:
    i = 1
    while i < len(nums):
        if i == 0 or nums[i - 1] <= nums[i]:
            i += 1

        else:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i -= 1

    return nums


print(gnome_sort([5, 3, 8, 0, 7, 4, 9, 1, 6, 2]))

