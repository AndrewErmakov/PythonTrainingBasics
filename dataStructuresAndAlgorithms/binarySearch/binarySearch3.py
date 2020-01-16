def leftside_binary_search(list_num: list, key: int) -> tuple:
    """Реализация левостороннего двоичного поиска"""
    left_border = -1
    right_border = len(list_num)

    while right_border - left_border > 1:

        mid = (left_border + right_border) // 2

        if list_num[mid] < key:
            left_border = mid

        else:
            right_border = mid

    if list_num[left_border] != key and list_num[right_border] != key:
        return 'NO'

    else:
        return 'YES'
