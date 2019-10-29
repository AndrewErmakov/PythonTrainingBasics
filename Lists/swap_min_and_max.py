list_elem = [int(i) for i in input().split()]

max_elem = max(list_elem)
index_max_elem = list_elem.index(max_elem)

min_elem = min(list_elem)
index_min_elem = list_elem.index(min_elem)

list_elem[index_max_elem], list_elem[index_min_elem] = list_elem[index_min_elem], list_elem[index_max_elem]

for elem in list_elem:
    print(elem, end=' ')

