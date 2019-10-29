list_numbers = []

number = int(input())

count = 0

while number != 0:
    list_numbers.append(number)
    number = int(input())

if len(list_numbers) >= 3:
    for i in range(1, len(list_numbers) - 1):
        if list_numbers[i - 1] < list_numbers[i] > list_numbers[i + 1]:
            count += 1

print(count)

