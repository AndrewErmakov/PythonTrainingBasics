sentence = input()

if sentence.count('f') == 1:
    print(-1)

elif sentence.count('f') == 0:
    print(-2)

elif sentence.count('f') > 1:
    firstIndexOfLetterF = sentence.find('f')
    secondPartOfSentence = sentence[firstIndexOfLetterF+1:]
    secondIndexOfLetterF = secondPartOfSentence.find('f')
    print(secondIndexOfLetterF + (len(sentence) - len(secondPartOfSentence)))
