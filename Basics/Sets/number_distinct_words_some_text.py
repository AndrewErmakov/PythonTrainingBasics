numbers_sentences = int(input())
set_words = set()
list_sentences = []

for i in range(numbers_sentences):
    sentence = input().split()
    list_sentences.append(sentence)

for sentence in list_sentences:
    for word in sentence:
        set_words.add(word)

print(len(set_words))


