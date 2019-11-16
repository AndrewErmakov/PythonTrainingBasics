count_numbers = int(input())
list_numbers = [int(i) for i in input().split()]

inserted_number, index_inserted_number = map(int, input().split())


def insert_element(nums: list, ins_num: int, index_ins_num):
    index_ins_num -= 1
    nums = nums[:index_ins_num] + [ins_num] + nums[index_ins_num:]
    return nums


for elem in insert_element(list_numbers, inserted_number, index_inserted_number):
    print(elem, end=' ')


