number = int(input())
reverse_number = ''
while number > 0:
    digit = number % 10
    reverse_number += str(digit)
    number //= 10

print(int(reverse_number))

