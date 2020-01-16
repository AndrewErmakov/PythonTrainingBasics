def determining_similarity_arrays_with_sets(nums1: list, nums2: list):
    if set(nums1) == set(nums2):
        return 'YES'
    else:
        return 'NO'


count_numbers_first_list = int(input())
first_list_numbers = [int(i) for i in input().split()]
count_numbers_second_list = int(input())
second_list_numbers = [int(i) for i in input().split()]
print(determining_similarity_arrays_with_sets(first_list_numbers, second_list_numbers))

