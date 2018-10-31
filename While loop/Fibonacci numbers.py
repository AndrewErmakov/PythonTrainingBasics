number = int(input())
fib1 = fib2 = 1
i = 2
if number == 1:
    fib_sum = 1
if number == 0:
    fib_sum = 0
if number == 2:
    fib_sum = 1
while i < number:
    fib_sum = fib2 + fib1
    fib1 = fib2
    fib2 = fib_sum
    i += 1
print(fib_sum)


