sentence = input()

partOfSentenceBetweenLetterH = sentence[sentence.find('h'):sentence.rfind('h') + 1:]

inversePartOfSentenceBetweenLetterH = partOfSentenceBetweenLetterH[::-1]

newSentence = sentence.replace(partOfSentenceBetweenLetterH, inversePartOfSentenceBetweenLetterH)

print(newSentence)


