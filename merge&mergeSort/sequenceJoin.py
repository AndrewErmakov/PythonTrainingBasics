from math import ceil


def merge(len_result_list):
    result_list = []
    index_first_list = index_second_list = 1

    while len(result_list) < len_result_list:

        if index_first_list ** 2 == index_second_list ** 3:
            result_list.append(index_first_list ** 2)

            index_first_list += 1
            index_second_list += 1

        elif index_first_list ** 2 < index_second_list ** 3:
            result_list.append(index_first_list ** 2)

            index_first_list += 1

        else:
            result_list.append(index_second_list ** 3)

            index_second_list += 1

    return result_list


serial_number = int(input())

print(merge(serial_number)[serial_number - 1])
