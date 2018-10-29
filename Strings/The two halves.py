import math

sentence = input()  # ввод предложения

partOfSentence1 = sentence[math.ceil(0.5 * len(sentence)):len(sentence)]
partOfSentence2 = sentence[:math.ceil(0.5 * len(sentence))]

print(partOfSentence1 + partOfSentence2)
