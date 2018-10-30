current_run = int(input())
desired_run = int(input())
count_of_days = 1

while current_run < desired_run:
    count_of_days += 1
    current_run += current_run / 10
print(count_of_days)
