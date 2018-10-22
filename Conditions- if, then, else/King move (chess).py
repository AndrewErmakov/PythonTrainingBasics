import math

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())
if (math.fabs(x2 - x1) == 1) and (math.fabs(y2 - y1) == 1):
    print('YES')
elif (math.fabs(x2 - x1) == 1) and (math.fabs(y2 - y1) == 0):
    print('YES')
elif (math.fabs(x2 - x1) == 0) and (math.fabs(y2 - y1) == 1):
    print('YES')

else:
    print('NO')