N = int(input())
sum_elements = 0
factorial = 1

for i in range(1, N + 1):
    factorial *= i
    sum_elements += factorial
print(sum_elements)
