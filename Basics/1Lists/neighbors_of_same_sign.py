list = [int(i) for i in input().split()]

for i in range(1, len(list)):

    if list[i] * list[i - 1] > 0:

        print(list[i-1], list[i])
        break

