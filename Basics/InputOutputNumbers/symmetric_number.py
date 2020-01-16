number = int(input())

thous_digit = number // 1000

hundred_digit = number // 100 % 10

tens_digit = number % 1000 % 100 // 10

last_digit = number % 1000 % 100 % 10

print(int(thous_digit == last_digit) + int(tens_digit == hundred_digit) - 1)


