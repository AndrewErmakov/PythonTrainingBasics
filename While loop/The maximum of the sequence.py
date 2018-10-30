number = int(input())
maximum = number

while number != 0:
    number = int(input())
    if number > maximum:
        maximum = number
print(maximum)
