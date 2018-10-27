number_of_cards = int(input())
sum_elements = 0
for i in range(1, number_of_cards + 1):
    sum_elements += i

for i in range(number_of_cards - 1):
    sum_elements -= int(input())
print(sum_elements)
