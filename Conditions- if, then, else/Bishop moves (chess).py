import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (math.fabs(x2 - x1) == math.fabs(y2 - y1)):
    print('YES')
else:
    print('NO')