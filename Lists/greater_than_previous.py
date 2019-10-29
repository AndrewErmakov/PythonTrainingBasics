list_numbers = input().split()
previous_number = 2 ** 32
for i in range(len(list_numbers)):
    if int(list_numbers[i]) > previous_number:
        print(list_numbers[i], end=' ')
    previous_number = int(list_numbers[i])
	
