def swap_columns(a, i, j):
    for k in range(len(a)):
        a[k][i], a[k][j] = a[k][j], a[k][i]
 
n, m = [int(i) for i in input().split()]
symbols_list = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
swap_columns(symbols_list, i, j)

for row in symbols_list:
    for elem in row:
        print(elem, end=' ')
    print()
