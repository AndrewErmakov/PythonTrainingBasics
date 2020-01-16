list = [int(i) for i in input().split()]

counter_of_elements = 0

for i in range(1, len(list) - 1):

    if list[i] > list[i - 1] and list[i] > list[i + 1]:

        counter_of_elements += 1

print(counter_of_elements)

