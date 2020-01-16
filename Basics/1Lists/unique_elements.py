list_elem = [int(i) for i in input().split()]
unique_elem = []
for elem in list_elem:
    if list_elem.count(elem) == 1:
        unique_elem.append(elem)

for element in unique_elem:
    print(element, end=' ')

