sentence = input()

max_len = 1 #длина "идеального" отряда
fragment_enlargement = 2 # увеличение фрагмента

result_squad = sentence[0] #требуемый отряд - результат работы программы

while fragment_enlargement <= len(sentence):
    for i in range(len(sentence)):
        while i + fragment_enlargement <= len(sentence):

            fragment_of_sentence = sentence[i:i + fragment_enlargement]

            if fragment_of_sentence[:len(fragment_of_sentence)] == fragment_of_sentence[::-1]:
                if len(fragment_of_sentence) > max_len:
                    result_squad = fragment_of_sentence
                    max_len = len(result_squad)
            break

    fragment_enlargement += 1

print(result_squad)


