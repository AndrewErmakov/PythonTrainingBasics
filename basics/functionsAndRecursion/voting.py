def voting(a):
    if sum(a) < 2:
        return 0
    else:
        return 1


numbers = [int(i) for i in input().split()]
res = voting(numbers)
print(res)
