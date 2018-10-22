N = int(input())
sum = 0
factorial = 1

for i in range(1, N+1):
    factorial *= i
    sum += factorial
print(sum)
