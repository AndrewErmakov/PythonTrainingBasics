def power(a, n):
    result = 1
    for i in range(abs(n)):
        if n > 0:
            result *= a
        elif n < 0:
            result /= a
    return result

a = float(input())
n = int(input())

print(power(a, n))
