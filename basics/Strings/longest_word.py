sentence = input()
words = sentence.split()

max_len_word = 0
word_with_max_len = ''

for word in words:
    if len(word) > max_len_word:
        max_len_word = len(word)
        word_with_max_len = word
print(word_with_max_len)
print(max_len_word)


