width_diploma, height_diploma, count_diplomas = map(int, input().split())


def board_size_determination(w: int = width_diploma, h: int = height_diploma, n: int = count_diplomas):
    left_border = min(w, h)
    right_border = n * max(w, h)

    while left_border < right_border:

        mid = (left_border + right_border) // 2

        if n <= (mid // w) * (mid // h):
            right_border = mid

        else:
            left_border = mid + 1

    return left_border


side_board = board_size_determination()
print(side_board)

