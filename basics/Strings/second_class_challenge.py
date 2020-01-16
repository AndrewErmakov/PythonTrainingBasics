number = int(input())

digits_with_one_circle = "069"
digits_with_two_circles = "8"

count_circles = 0
try:
    for symbol in str(number):
        if symbol in digits_with_one_circle:
            count_circles += 1

        if symbol in digits_with_two_circles:
            count_circles += 2
except str(number) == '':
    count_circles = 0

print(count_circles)


