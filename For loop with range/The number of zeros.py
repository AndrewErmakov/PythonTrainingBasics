N = int(input())
countOfZero = 0
for i in range(N):
    number = int(input())
    if (number == 0):
        countOfZero += 1
print(countOfZero)