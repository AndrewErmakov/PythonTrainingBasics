count_elements = int(input())

list_elements = [int(i) for i in input().split()]

for i in range(count_elements):

    if count_elements // 2 == i:
        break

    list_elements[i], list_elements[count_elements - i - 1] = list_elements[count_elements - i - 1], list_elements[i]


for elem in list_elements:
    print(elem, end=' ')
    
