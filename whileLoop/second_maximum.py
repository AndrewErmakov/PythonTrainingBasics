sequence = []
number = int(input())

sequence_without_first_max = []

while number != 0:
    sequence.append(number)
    number = int(input())

sequence = sorted(sequence)
print(sequence[-2])

