def get_palindrome(sentence):
    if sentence == sentence[::-1]:
        return sentence
    else:
        for i in range(len(sentence) - 1):
            list_sentence = list(sentence)
            list_sentence[i], list_sentence[i + 1] = list_sentence[i + 1], list_sentence[i]
            new_sentence = ''.join(list_sentence)
            if new_sentence == new_sentence[::-1]:
                return new_sentence

        return -1


print(get_palindrome(input()))
