number = int(input())
maximum = number
numberOfElementsEqualToTheMax = 1

while number != 0:
    number = int(input())
    if number == maximum:
        numberOfElementsEqualToTheMax += 1
    if number > maximum:
        maximum = number
        numberOfElementsEqualToTheMax = 1

print(numberOfElementsEqualToTheMax)

