numberOfCards = int(input())
sum = 0
for i in range(1, numberOfCards + 1):
    sum += i

for i in range(numberOfCards - 1):
    sum -= int(input())
print(sum)
