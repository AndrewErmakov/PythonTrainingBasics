n, m = [int(i) for i in input().split()]
symbols_list = [[int(j) for j in input().split()] for i in range(n)]

const = int(input())

for i in range(n):
    for j in range(m):
        symbols_list[i][j] *= const

for row in symbols_list:
    for elem in row:
        print(elem, end=' ')
    print()

