sentence = input()

while sentence.find('  ') != -1:
    sentence = sentence.replace('  ', ' ')

print(sentence)

