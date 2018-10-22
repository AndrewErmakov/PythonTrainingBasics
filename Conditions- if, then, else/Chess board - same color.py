x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if ((x1 + y1) % 2 == 0) and ((x2 + y2) % 2 == 0) or ((x1 + y1) % 2 == 1) and ((x2 + y2) % 2 == 1):
    print('YES')
else:
    print('NO')