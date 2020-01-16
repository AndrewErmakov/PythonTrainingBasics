number_sportsmen, count_attempts = map(int, input().split())

list_line_number = list_column_number = max_elem = -1

list_numbers_and_attempts = [[int(j) for j in input().split()] for i in range(number_sportsmen)]

for i in range(number_sportsmen):
    for j in range(count_attempts):
        if list_numbers_and_attempts[i][j] > max_elem:
            max_elem = list_numbers_and_attempts[i][j]
            list_line_number = i
            list_column_number = j

print(max_elem)
print(list_line_number, list_column_number)
