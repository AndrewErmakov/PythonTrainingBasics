number_sentences = int(input())

dict_words = dict()

for i in range(number_sentences):
    sentence = input().split()

    for elem in sentence:
        if elem not in dict_words:
            dict_words[elem] = 1
        else:
            dict_words[elem] += 1

list_frequence_word = list()

for word, frequence_word in sorted(dict_words.items()):
    list_frequence_word.append((frequence_word, word))


for frequence_word, word in sorted(list_frequence_word, key=lambda x: (-x[0], x[1])):
    print(word)
