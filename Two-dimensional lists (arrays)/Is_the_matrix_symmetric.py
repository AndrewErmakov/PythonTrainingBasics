size_list = int(input())

numbers_list = [[int(j) for j in input().split()] for i in range(size_list)]
answer = "yes"
for i in range(size_list):
    for j in range(size_list):
        if numbers_list[i][j] != numbers_list[j][i]:
            answer = "no"
            break

print(answer)
