number = int(input())

number_of_even_elements = 0
while number != 0:
    if number % 2 == 0:
        number_of_even_elements += 1
    number = int(input())

print(number_of_even_elements)
