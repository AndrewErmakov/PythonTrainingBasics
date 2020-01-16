def prime_definition(number):
    answer = "prime"
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            answer = "composite"
            break
    return answer


num = int(input())
result = prime_definition(num)
print(result)
