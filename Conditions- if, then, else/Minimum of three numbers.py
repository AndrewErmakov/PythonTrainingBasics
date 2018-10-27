a = int(input())
b = int(input())
c = int(input())
minimal = a
if b < minimal:
    minimal = b
if c < minimal:
    minimal = c
print(minimal)
