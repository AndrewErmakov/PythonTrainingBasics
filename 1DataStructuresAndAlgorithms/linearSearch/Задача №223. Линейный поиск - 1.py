count_list_elements = int(input())

list_numbers = [int(i) for i in input().split()]

x = int(input())

count_elements_equal_to_x = 0

for i in range(count_lits_elements):
    if list_numbers[i] == x:
        count_elements_equal_to_x += 1

print(count_elements_equal_to_x)
