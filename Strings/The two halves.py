import math

sentence = input()  # ввод предложения

number_of_characters_in_half_sentence = math.ceil(0.5 * len(sentence))

partOfSentence1 = sentence[number_of_characters_in_half_sentence:len(sentence)]
partOfSentence2 = sentence[:number_of_characters_in_half_sentence]

print(partOfSentence1 + partOfSentence2)
