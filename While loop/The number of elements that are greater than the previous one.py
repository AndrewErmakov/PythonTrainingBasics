number1 = int(input())

countOf2x = 0
while number1 != 0:
    number2 = int(input())
    if number2 > number1:
        countOf2x += 1
    number1 = number2
print(countOf2x)
