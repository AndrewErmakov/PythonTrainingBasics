number_eng_words = int(input())

dict_latin_eng = dict()

for i in range(number_eng_words):
    eng_word, all_translations_latin_words = input().split(' - ')

    latin_translations = all_translations_latin_words.split(', ')

    for latin_word in latin_translations:

        if latin_word not in dict_latin_eng:
            dict_latin_eng[latin_word] = eng_word

        else:
            dict_latin_eng[latin_word] += ', ' + eng_word

print(len(dict_latin_eng))

# print(eng_word)
# print(latin_translations)

for key_latin, value_eng in sorted(dict_latin_eng.items()):
    print(key_latin + ' - ' + value_eng)
