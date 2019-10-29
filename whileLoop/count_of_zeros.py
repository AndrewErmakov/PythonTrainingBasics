number = int(input())
sum_digits = 0
count_zeros = 0
while number > 0:
    digit = number % 10
    if digit == 0:
        count_zeros += 1
    number //= 10

print(count_zeros)

