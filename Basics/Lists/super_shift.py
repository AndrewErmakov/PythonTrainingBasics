count_elements = int(input())

list_elements = [int(i) for i in input().split()]
count_step_shift = int(input())

interim_number_list = ['' for k in range(abs(count_step_shift))]

sign = 1
if count_step_shift < 0:
    sign = -1

if count_step_shift != 0:
    for i in range(0, count_elements * sign, sign):

        if type(interim_number_list[i % count_step_shift]) != int:
            interim_number_list[i % count_step_shift] = list_elements[i]

        list_elements[(i + count_step_shift) % count_elements], interim_number_list[i % count_step_shift] = \
            interim_number_list[i % count_step_shift], list_elements[(i + count_step_shift) % count_elements]

for elem in list_elements:
    print(elem, end=' ')

