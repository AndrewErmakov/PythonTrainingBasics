list_elements = [int(i) for i in input().split()]

number_distinct_elements = 1

for i in range (1, len(list_elements)):
    if list_elements[i] != list_elements[i - 1]:
        number_distinct_elements += 1
    
print(number_distinct_elements)

