count_numbers = int(input())
list_numbers = [int(i) for i in input().split()]


def radix_sort(nums):
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1

    while not maxLength:
        maxLength = True
        
		buckets = [list() for _ in range(RADIX)]

        for i in nums:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                nums[a] = i
                a += 1

        placement *= RADIX

    return nums


for elem in radix_sort(list_numbers):
    print(elem, end=' ')


