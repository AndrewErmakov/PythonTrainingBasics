number_1 = int(input())

number_2 = int(input())

max = int(number_1 >= number_2) * number_1 + int(number_1 <= number_2) * number_2 - int(number_2 == number_1) * number_1

print(max)

