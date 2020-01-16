n, m = map(int, input().split())
chess_board = [['*'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
            chess_board[i][j] = '.'

for row in chess_board:
    for elem in row:
        print(elem, end=' ')
    print()

