def KUniqueCharacters(strParam):
    count_unique_symbols = int(strParam[0])
    result = ''

    for i in range(1, len(strParam)):
        current_substring = ''
        set_unique_symbols = set()
        while len(set_unique_symbols) <= count_unique_symbols and i < len(strParam):
            set_unique_symbols.add(strParam[i])
            current_substring += strParam[i]
            i += 1
            if i == len(strParam) and len(current_substring) > len(result):
                return current_substring

        if len(current_substring[:-1]) > len(result):
            result = current_substring[:-1]

    # code goes here
    return result


# keep this function call here
print(KUniqueCharacters(input()))
