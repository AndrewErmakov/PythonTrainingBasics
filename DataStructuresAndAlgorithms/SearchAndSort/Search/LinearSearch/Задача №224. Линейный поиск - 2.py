count_list_elements = int(input())

list_numbers = [int(i) for i in input().split()]

number = int(input())

j = -1
for i in range(count_list_elements):
    if list_numbers[i] == number:
        j = i
        break


if j != -1:
    print('YES')

else:
    print('NO')
# def search_number(array_numbers, x):
#     for i in range(count_list_elements):
#         if array_numbers[i] == x:
#             j = i
#             break
#     return j
#
#
# def get_answer(k: int) -> str:
#     if k != -1:
#         return 'YES'
#
#     else:
# #         return 'NO'
#
#
# print(get_answer(search_number(list_numbers, number)))
