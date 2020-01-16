from math import sqrt
number = int(input())

list_numbers = []
standard_deviate = 0
while number != 0:
    list_numbers.append(number)
    number = int(input())

arithmetic_average_sequence = sum(list_numbers) / len(list_numbers)

for i in range(len(list_numbers)):
    standard_deviate += (list_numbers[i] - arithmetic_average_sequence) ** 2

standard_deviate = sqrt(standard_deviate / (len(list_numbers) - 1))

print(standard_deviate)

