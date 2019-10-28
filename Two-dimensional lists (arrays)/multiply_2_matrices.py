n, m, r = [int(i) for i in input().split()]
matrix_1 = [[int(j) for j in input().split()] for i in range(n)]

matrix_2 = [[int(k) for k in input().split()] for j in range(m)]

result_matrix = [[0] * r for h in range(n)]

for i in range(n):
    for j in range(r):
        for k in range(m):
            result_matrix [i][j] += matrix_1[i][k] * matrix_2[k][j]

for row in result_matrix:
    for elem in row:
        print(elem, end=' ')
    print()