sentence = input()
result_sentence = ''
str_current_number = ''
counter = 0 #счетчик обработанных символов

for elem in sentence:
    counter += 1
    while elem.isdigit():
        str_current_number += elem
        break

    if len(str_current_number) != 0:
        if not elem.isdigit() or counter == len(sentence):

            current_number = int(str_current_number)
            reversed_binary_result = ''

            while current_number > 0:
                reversed_binary_result += str(current_number % 2)
                current_number //= 2

            for symbol in reversed(reversed_binary_result):
                result_sentence += symbol

            current_number = 0
            str_current_number = reversed_binary_result = ''

    if not elem.isdigit():
        result_sentence += elem

print(result_sentence)


