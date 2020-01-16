def search_min(a):
    min_number = a[0]
    for i in range(1, len(a)):
        if a[i] < min_number:
            min_number = a[i]

    return min_number


list_numbers = [int(i) for i in input().split()]

min_elem = search_min(list_numbers)
print(min_elem)
