number1 = int(input())
intermediate_length = 1
fragment_length = 0
while number1 != 0:
    number2 = int(input())
    number1, number2 = number2, number1
    if number2 == number1:
        intermediate_length += 1
    if intermediate_length > fragment_length:
        fragment_length = intermediate_length
    if number1 != number2:
        intermediate_length = 1
print(fragment_length)
