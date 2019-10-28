number_sportsmen, count_attempts = map(int, input().split())

list_line_number = max_sum = -1

list_numbers_and_attempts = [[int(j) for j in input().split()] for i in range(number_sportsmen)]

for i in range(number_sportsmen):
    sum_numbers_in_line = 0
    for j in range(count_attempts):
        sum_numbers_in_line += list_numbers_and_attempts[i][j]

    if sum_numbers_in_line > max_sum:
        max_sum = sum_numbers_in_line
        list_line_number = i


print(max_sum)
print(list_line_number)
