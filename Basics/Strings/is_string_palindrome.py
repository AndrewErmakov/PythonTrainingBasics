sentence = input()
sentence_without_spaces = sentence.replace(' ', '')
reverse_sentence = ''

for elem in reversed(sentence_without_spaces):
    reverse_sentence += elem

if reverse_sentence == sentence_without_spaces:
    print("yes")

else:
    print("no")


