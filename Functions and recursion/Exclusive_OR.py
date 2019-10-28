def xor(x, y):
    if bool(x) + bool(y) == 1 and bool(x) * bool(y) != 1:
        return 1

    else:
        return 0


a, b = map(int, input().split())
result = xor(a, b)

print(result)
