sentence = input()

for elem in sentence:
    if sentence.count(elem) == 2:
        print(elem)
        break


