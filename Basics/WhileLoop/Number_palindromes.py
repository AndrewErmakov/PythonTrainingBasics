max_number = int(input())

count_palindromes = 0
for number in range(1, max_number + 1):
    current_number = number
    reverse_number = ''
    while number > 0:
        digit = number % 10
        reverse_number += str(digit)
        number //= 10

    if current_number == int(reverse_number):
        count_palindromes += 1

print(count_palindromes)

