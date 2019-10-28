def fib(number):
    f0, f1 = 0, 1
    f_prev2 = f0
    f_prev1 = f1
    
    if number == 0:
        f_next = 0
    elif number == 1:
        f_next = 1
    elif number > 1:
        while number > 1:
            f_next = f_prev1 + f_prev2
            number -= 1
            f_prev1, f_prev2 = f_next, f_prev1
        
    print(f_next)
        
n = int(input())
fib(n)
        