sentence = input().split()

list_words_of_sentence = list(sentence)

dict_words = dict()
#print(list_sentence)

for elem in list_words_of_sentence:
    if elem not in dict_words:
        dict_words[elem] = 0
        print(dict_words[elem])
    else:
        dict_words[elem] += 1
        print(dict_words[elem])
