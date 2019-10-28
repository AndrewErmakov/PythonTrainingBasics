import math
def find_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(find_distance(a, b, c, d))
