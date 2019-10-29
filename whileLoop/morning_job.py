xMiles = int(input())
yMiles = int(input())
countOfDays = 1

while (xMiles < yMiles):
    countOfDays += 1
    xMiles += (xMiles) / 10
print(countOfDays)
    
