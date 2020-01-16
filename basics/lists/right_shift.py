count_elements = int(input())

list_elements = [int(i) for i in input().split()]
interim_number = ''

for i in range(count_elements):

    if type(interim_number) != int:
        interim_number = list_elements[i]

    list_elements[(i + 1) % count_elements], interim_number = interim_number, list_elements[(i + 1) % count_elements]

for elem in list_elements:
    print(elem, end=' ')

