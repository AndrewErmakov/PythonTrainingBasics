ip_address = input()
answer = ''

numbers_of_ip = ip_address.split('.')

for elem in numbers_of_ip:
    if elem.isdigit() and 0 <= int(elem) <= 255:
        answer = 1

    else:
        answer = 0
        break

if ip_address.count('.') != 3:
    answer = 0

print(answer)


