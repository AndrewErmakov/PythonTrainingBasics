import math

speedPerDay = int(input())
wayInKilometres = int(input())
days = math.ceil(wayInKilometres / speedPerDay)
print(days)
