first_word = input()
second_word = input()


def counting_sort(word: str):
    count_list = [0] * 36
    sorted_sequence = []

    for symbol in word:
        if 'a' <= symbol <= 'z':
            count_list[ord(symbol) - 87] += 1

        if symbol.isdigit():
            count_list[int(symbol)] += 1

    for i in range(36):
        if count_list[i] > 0:
            if i < 10:
                sorted_sequence += ((str(i) + ' ') * count_list[i]).split()

            else:
                sorted_sequence += ((chr(i + 87) + ' ') * count_list[i]).split()

    return sorted_sequence


def are_anagrams(symbols_first_word: list, symbols_second_word: list):

    len_symbols_first_word, len_symbols_second_word = len(symbols_first_word), len(symbols_second_word)

    if len_symbols_first_word != len_symbols_second_word:
        return "NO"

    else:
        for i in range(len_symbols_first_word):
            if symbols_first_word[i] != symbols_second_word[i]:
                return "NO"

        return "YES"


print(are_anagrams(counting_sort(first_word), counting_sort(second_word)))




