sentence = input()
findingTheSpace = sentence.find(' ')

firstPart = (sentence[:findingTheSpace])
secondPart = (sentence[findingTheSpace:])
print(secondPart + ' ' + firstPart)
