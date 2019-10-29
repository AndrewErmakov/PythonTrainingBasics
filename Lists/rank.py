count_elements = int(input())

list_elements = [int(i) for i in input().split()]

number = int(input())
serial_number_in_rank = count_elements + 1

for i in range(count_elements):
    if number > list_elements[i]:
        serial_number_in_rank = i + 1
        break

print(serial_number_in_rank)

