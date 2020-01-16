list_elements = [int(i) for i in input().split()]  # список с номерами шаров
list_consecutive_balls = []

list_indices_consecutive_balls = []  # список индексов (в списке list_elements) подряд идущих шаров

count_destroyed_balls = 0  # количество уничтоженных шаров
amount_of_destruction = 1  # количество уничтожений (изначально для цикла while сделал единицу)

while amount_of_destruction > 0:

    amount_of_destruction = 0

    list_consecutive_balls.clear()
    list_consecutive_balls = [list_elements[0]]  # список подряд идущих шаров

    list_indices_consecutive_balls.clear()

    for i in range(1, len(list_elements)):

        if list_elements[i] == list_elements[i - 1]:
            list_consecutive_balls.append(list_elements[i])
            list_indices_consecutive_balls.append(i)

        if list_elements[i] != list_elements[i - 1] or i == len(list_elements) - 1:

            if len(list_consecutive_balls) >= 3:
                amount_of_destruction += 1  # увеличение числа кол-ва взрывов шаров
                count_destroyed_balls += len(list_consecutive_balls)  # увеличение числа уничтоженных шаров
                for index in reversed(list_indices_consecutive_balls):  # удаление из списка подряд идущих элементов по индексу
                    del list_elements[index]
                break

            list_consecutive_balls.clear()
            list_indices_consecutive_balls.clear()
            list_consecutive_balls.append(list_elements[i])
            list_indices_consecutive_balls.append(i)

print(count_destroyed_balls)

