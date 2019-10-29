count_elements, serial_number1, serial_number2, serial_number3, serial_number4 = map(int, input().split())

list_elements = []

for i in range(count_elements):
    list_elements.append(i + 1)

fragment1 = list_elements[serial_number1 - 1:serial_number2] # выделение 1го фрагмента

for i in range(len(fragment1)): #

    if len(fragment1) // 2 == i:
        break

    fragment1[i], fragment1[len(fragment1) - i - 1] = fragment1[len(fragment1) - i - 1], fragment1[i]

index_fragment1 = index_fragment2 = 0
for i in range(serial_number1 - 1, serial_number2): #первый переворот
    list_elements[i] = fragment1[index_fragment1]
    index_fragment1 += 1

fragment2 = list_elements[serial_number3 - 1:serial_number4] # выделение 2го фрагмента
for i in range(len(fragment2)): #

    if len(fragment2) // 2 == i:
        break

    fragment2[i], fragment2[len(fragment2) - i - 1] = fragment2[len(fragment2) - i - 1], fragment2[i]

for i in range(serial_number3 - 1, serial_number4): #первый переворот
    list_elements[i] = fragment2[index_fragment2]
    index_fragment2 += 1

for elem in list_elements:
    print(elem, end=' ')

