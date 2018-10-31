sentence = input()
newSentence = ''
for i in range(len(sentence)):
    if i % 3 != 0:
        newSentence += sentence[i]
print(newSentence)

