number_of_sentences = int(input())

dict_words = dict()

for i in range(number_of_sentences):
    list_words_of_sentence = list(input().split())
    for elem in list_words_of_sentence:
        if elem not in dict_words:
            dict_words[elem] = 1

        else:
            dict_words[elem] += 1

max_frequence_word = 0

for word, frequence_word in sorted(dict_words.items()):
    if frequence_word > max_frequence_word:
        max_frequence_word = frequence_word

#print(dict_words)

for word, frequence_word in sorted(dict_words.items()):
    if int(dict_words[word]) == int(max_frequence_word):
        print(word)
        break

