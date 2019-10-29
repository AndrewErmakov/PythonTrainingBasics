number = int(input())

maximum = number
indexOfMaximum = 1
index = 1

while number != 0:
    number = int(input())
    index += 1
    if number > maximum:
        maximum = number
        indexOfMaximum =index
print(indexOfMaximum)

