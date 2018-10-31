sentence = input()
mark = 0

if sentence.rfind('f') == sentence.find('f') and sentence.find('f') >= 0:
    print(sentence.find('f'))

elif sentence.rfind('f') != sentence.find('f'):
    print(sentence.find('f'))
    print(sentence.rfind('f'))
