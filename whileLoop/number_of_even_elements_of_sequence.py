number = int(input())

count_even_elements = 0
while number != 0:
    if number % 2 == 0:
        count_even_elements += 1
    number = int(input())
    
print(count_even_elements)

