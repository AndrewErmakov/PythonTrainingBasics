len_table, count_socks, count_points = map(int, input().split())


def determination_thickness(length_table, number_socks, number_points):
    count_list = [0] * (length_table + 1)

    for _ in range(number_socks):
        left_border, right_border = map(int, input().split())

        for i in range(left_border, right_border + 1):
            count_list[i] += 1

    for j in range(number_points):
        index_point = int(input())

        print(count_list[index_point])


determination_thickness(len_table, count_socks, count_points)


