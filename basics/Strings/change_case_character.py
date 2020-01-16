symbol = input()
try:
    case_sensitive_character = symbol.swapcase()

except ValueError:
    case_sensitive_character = symbol

print(case_sensitive_character)


