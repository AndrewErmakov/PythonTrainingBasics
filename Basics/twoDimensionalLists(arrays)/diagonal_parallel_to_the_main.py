n = int(input())
symbols_list = [['.'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        symbols_list[i][j] = abs(i - j)

for row in symbols_list:
    for elem in row:
        print(elem, end=' ')
    print()
