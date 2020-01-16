count_requests = int(input())
set_numbers = set()

for i in range(count_requests):
    request = input().split()

    if request[0] == "ADD":
        set_numbers.add(request[1])

    elif request[0] == "PRESENT":
        if request[1] in set_numbers:
            print("YES")
        else:
            print("NO")

    elif request[0] == "COUNT":
        print(len(set_numbers))

