lengthOfLine = 0
sumOfSequence = 0
number = int(input())
while (number != 0):
    sumOfSequence += number
    lengthOfLine += 1
    number = int(input())
print(sumOfSequence / lengthOfLine)

