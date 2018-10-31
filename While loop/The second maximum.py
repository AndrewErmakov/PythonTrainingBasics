element1 = element2 = 0
number = int(input())
while number != 0:
    if number >= element1:
        element2 = element1
        element1 = number
    elif element2 < number < element1:
        element2 = number
    number = int(input())
print(element2)
