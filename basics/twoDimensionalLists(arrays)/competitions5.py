number_sportsmen, count_attempts_each_sportsman = map(int, input().split())

list_line_number = list_column_number = max_elem = -1
max_sum_attempts_best_sportsman = -1

list_numbers_and_attempts = [[int(j) for j in input().split()] for i in range(number_sportsmen)]
count_winners = 1
list_line_numbers_of_winners = []

for i in range(number_sportsmen):
    attempts_each_sportsman = []
    for j in range(count_attempts_each_sportsman):
        attempts_each_sportsman.append(list_numbers_and_attempts[i][j])

    best_attempt = max(attempts_each_sportsman)

    if best_attempt == max_elem:
        list_line_numbers_of_winners.append(i)

    if best_attempt > max_elem:
        list_line_numbers_of_winners.clear()
        list_line_numbers_of_winners.append(i)
        max_elem = best_attempt

print(len(list_line_numbers_of_winners))
for elem in list_line_numbers_of_winners:
    print(elem, end=' ')
