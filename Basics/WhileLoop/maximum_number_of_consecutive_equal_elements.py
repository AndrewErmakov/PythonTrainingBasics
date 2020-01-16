number1 = int(input())
intermediate_length = 1
final_length = 1
while number1 != 0:
    number2 = int(input())
    if number2 == number1:
        intermediate_length += 1
    if intermediate_length > final_length:
        final_length = intermediate_length
    if number1 != number2:
        intermediate_length = 1
    number1, number2 = number2, number1 
print(final_length)

