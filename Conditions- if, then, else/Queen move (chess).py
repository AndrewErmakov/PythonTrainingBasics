x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

if (abs(x2 - x1) == abs(y2 - y1)):
    print('YES')
elif (x2 == x1):
    print('YES')
elif (y2 == y1):
    print('YES')
else:
    print('NO')