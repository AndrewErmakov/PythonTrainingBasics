number_sportsmen, count_attempts_each_sportsman = map(int, input().split())

list_line_number = list_column_number = max_elem = -1
max_sum_attempts_best_sportsman = -1

list_numbers_and_attempts = [[int(j) for j in input().split()] for i in range(number_sportsmen)]
count_winners = 1

for i in range(number_sportsmen):
    attempts_each_sportsman = []
    for j in range(count_attempts_each_sportsman):
        attempts_each_sportsman.append(list_numbers_and_attempts[i][j])

    best_attempt = max(attempts_each_sportsman)

    if best_attempt == max_elem:
        count_winners += 1

    if best_attempt > max_elem:
        max_elem = best_attempt
        count_winners = 1

print(count_winners)
