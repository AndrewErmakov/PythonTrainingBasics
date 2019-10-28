def exponentiation(a, n):
    if a == 0:
        return 0
    if n == 0:
        return 1

    else:
        if n > 0:
            return a * exponentiation(a, n - 1)

        if n < 0:
            return exponentiation(a, n + 1) / a
    # return res


number, exponent = input().split()
number = float(number)
exponent = int(exponent)

result = exponentiation(number, exponent)
print(result)
