def bin_coeff(n, k):
    if k == 0 or k == n:
        return 1

    else:
        return bin_coeff(n - 1, k - 1) + bin_coeff(n - 1, k)


num1, num2 = map(int, input().split())

result = bin_coeff(num1, num2)

print(result)

