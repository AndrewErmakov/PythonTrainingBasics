number = int(input())
inverse_binary_number = ''
while number > 0:
    digit = number % 2
    inverse_binary_number += str(digit)
    number //= 2

print(inverse_binary_number)

