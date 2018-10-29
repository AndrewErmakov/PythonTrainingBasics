sentence = input()

indexOfFirstLetter = sentence.find('h')
indexOfLastLetter = sentence.rfind('h')

partOfSentence = sentence[indexOfFirstLetter + 1:indexOfLastLetter]

partOfSentenceWithH = partOfSentence.replace('h', 'H')

newSentence = sentence[:indexOfFirstLetter+1] + partOfSentenceWithH + sentence[indexOfLastLetter:]
print(newSentence)
