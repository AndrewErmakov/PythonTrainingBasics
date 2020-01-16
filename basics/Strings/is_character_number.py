symbol = input()
try:
    number = int(symbol)
    answer = "yes"

except ValueError:
    answer = "no"

print(answer)


