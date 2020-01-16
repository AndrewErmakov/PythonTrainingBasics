list_numbers = []
list_indices_local_maximums = []
number = int(input())

min_distance_local_maximums = False

while number != 0:
    list_numbers.append(number)
    number = int(input())

if len(list_numbers) >= 3:
    for i in range(1, len(list_numbers) - 1):
        if list_numbers[i - 1] < list_numbers[i] > list_numbers[i + 1]:
            list_indices_local_maximums.append(i)

if len(list_indices_local_maximums) < 2:
    print(0)
else:
    for i in range(1, len(list_indices_local_maximums)):
        if not min_distance_local_maximums: #если не заявлено минимальное расстояние между локальными максимумами
            min_distance_local_maximums = list_indices_local_maximums[i] - list_indices_local_maximums[i - 1]

        else: #если не заявлено минимальное расстояние между локальными максимумами
            if list_indices_local_maximums[i] - list_indices_local_maximums[i - 1] < min_distance_local_maximums:
                min_distance_local_maximums = list_indices_local_maximums[i] - list_indices_local_maximums[i - 1]

    print(min_distance_local_maximums)

