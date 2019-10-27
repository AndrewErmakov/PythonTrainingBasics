number_pairs_words = int(input())

dict_synonyms = dict()

for i in range(number_pairs_words):
    pair_words_list = list(input().split())
    dict_synonyms[pair_words_list[0]] = pair_words_list[1]

word_synonym_for_finding = input("Введите слово для нахождения:")


for key, value in dict_synonyms.items():
    if key == word_synonym_for_finding:
        print(value)

    elif value == word_synonym_for_finding:
        print(key)

    else:
        continue

