N = int(input())
count_of_zero = 0
for i in range(N):
    number = int(input())
    if number == 0:
        count_of_zero += 1
print(count_of_zero)
