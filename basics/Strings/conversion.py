sentence = input()
first_index, last_index = map(int, input().split())

substring = sentence[first_index - 1:last_index]

converted_substring = substring[::-1]

new_sentence = sentence.replace(substring, converted_substring)
print(new_sentence)


