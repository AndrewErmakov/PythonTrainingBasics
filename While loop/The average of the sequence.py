length_of_sequence = 0
sum_of_sequence = 0
number = int(input())
while number != 0:
    sum_of_sequence += number
    length_of_sequence += 1
    number = int(input())
print(sum_of_sequence / length_of_sequence)
