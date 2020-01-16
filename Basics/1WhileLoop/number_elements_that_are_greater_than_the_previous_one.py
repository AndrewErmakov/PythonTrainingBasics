number1 = int(input())

count_elements = 0
while number1 != 0:
    number2 = int(input())
    if number2 > number1:
        count_elements += 1
    number1 = number2
print(count_elements)

