def counting_sorting(nums: list):
    max_elem = max(nums)
    min_elem = min(nums)
    sequence = []
    count_elements = [0] * (max_elem - min_elem + 1)

    for number in nums:
        count_elements[number - min_elem] += 1

    for i in range(max_elem - min_elem + 1):
        if count_elements[i] > 0:
            # print(i + min_elem, count_elements[i])
            sequence += ((str(i + min_elem) + ' ') * count_elements[i]).split()

    return sequence


count_nums = int(input())
list_nums = [int(i) for i in input().split()]
for num in counting_sorting(list_nums):
    print(int(num), end=' ')
