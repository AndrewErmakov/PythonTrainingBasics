def fast_pow(a, n):
    if n == 0:
        return 1

    if n % 2 == 1:
        return a * fast_pow(a, n - 1)

    else:
        return fast_pow(a * a, n // 2)


number, exponent = map(float, input().split())

exponent = int(exponent)
result = fast_pow(number, exponent)

print(result)
