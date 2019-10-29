number = int(input())
sum_digits = 0
count_zeros = 0
min_digit = 9
max_digit = 0

while number > 0:
    digit = number % 10
    if digit < min_digit:
        min_digit = digit

    if digit > max_digit:
        max_digit = digit

    number //= 10

print(min_digit, max_digit)

