from math import ceil

height = int(input())
day_distance = int(input())
night_distance = int(input())

num_days = ceil((height - day_distance) / (day_distance - night_distance)) + 1
print(num_days)


