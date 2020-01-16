number_roubles = int(input())
number_cents = int(input())

number_cakes = int(input())

print(number_roubles * number_cakes + (number_cakes * number_cents) // 100, (number_cakes * number_cents) % 100)


