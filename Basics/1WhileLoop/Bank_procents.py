from math import floor
x = int(input())
percents = int(input())
y = int(input())

year = 0
while x < y:
    x = x * (percents + 100) / 100
    x = floor(x * 100) / 100
    year += 1

print(year)


