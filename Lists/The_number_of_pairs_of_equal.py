a = input().split()

print(sum(a.count(x) - 1 for x in a) // 2)

