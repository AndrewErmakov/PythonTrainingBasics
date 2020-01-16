n, m = [int(i) for i in input().split()]

list_numbers = [[int(j) for j in input().split()] for i in range(n)]

max_elem = list_numbers[0][0]
i_best = 0
j_best = 0
for i in range(n):
    for j in range(m):
        if list_numbers[i][j] > max_elem:
            max_elem = list_numbers[i][j]
            i_best, j_best = i, j
            
print(i_best, j_best)
