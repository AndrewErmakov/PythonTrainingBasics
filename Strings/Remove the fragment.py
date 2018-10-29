sentence = input()

partOfSentence = sentence[sentence.find('h'):sentence.rfind('h')+1:]

newSentence = sentence.replace(partOfSentence, '')

print(newSentence)

