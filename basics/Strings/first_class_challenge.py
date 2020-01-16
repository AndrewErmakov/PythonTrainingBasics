first_number, required_row_number = map(int, input().split())

sequence = str(first_number)

row_number = 1

while row_number < required_row_number:
    prev_digit = -1
    ordinary_digits = []
    new_sequence = ''

    for i in range(len(sequence)):
        if sequence[i] == prev_digit:
            ordinary_digits.append(sequence[i])

        else:
            if len(ordinary_digits) > 0:
                new_sequence += str(len(ordinary_digits)) + ordinary_digits[0]

            ordinary_digits.clear()
            ordinary_digits.append(sequence[i])

        prev_digit = sequence[i]

    new_sequence += str(len(ordinary_digits)) + ordinary_digits[0]
    sequence = new_sequence
    row_number += 1

print(sequence)


