number_elements = int(input())

all_set_elements = set(range(1, number_elements + 1))

result_set_elements = all_set_elements
set_answer = set(input().split())

while True:
    if "HELP" in set_answer:
        for i in sorted(result_set_elements):
            print(i, end=' ')
        break
    else:
        answer_overlap = input()
        if answer_overlap == "YES":
            result_set_elements &= set(int(element) for element in set_answer)

        if answer_overlap == "NO":
            result_set_elements -= set(int(element) for element in set_answer)

        set_answer = set(input().split())


