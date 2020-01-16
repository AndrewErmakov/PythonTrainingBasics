n = int(input())
symbols_list = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if n - i - 1 == j :
            symbols_list[i][j] = 1
        elif n - i - 1 > j:
            symbols_list[i][j] = 0
        
        else:
            symbols_list[i][j] = 2
for row in symbols_list:
    for elem in row:
        print(elem, end=' ')
    print()

