symbol = input()
try:
    uppercase_character = symbol.title()

except ValueError:
    uppercase_character = symbol

print(uppercase_character)


