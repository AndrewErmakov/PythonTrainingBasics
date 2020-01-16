sentence = input()
number = int(input())
decryption_result = ''

for elem in sentence:
    code_for_decrypt_elem = ord(elem) % 91 + 26 - number
    if code_for_decrypt_elem not in range(65, 91):
        code_for_decrypt_elem -= 26
    new_elem = chr(code_for_decrypt_elem)
    decryption_result += new_elem

print(decryption_result)


