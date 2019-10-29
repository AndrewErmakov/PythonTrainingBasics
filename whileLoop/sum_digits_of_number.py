number = int(input())
sum_digits = 0
while number > 0:
    digit = number % 10
    sum_digits += digit
    number //= 10

print(sum_digits)

