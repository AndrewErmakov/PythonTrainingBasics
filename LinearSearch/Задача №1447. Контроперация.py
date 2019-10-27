count_marks_and_marks = input().split()

marks = [int(i) for i in count_marks_and_marks[1:]]


def change_marks(list_marks: list = marks) -> list:
    max_elem = max(list_marks)
    min_elem = min(list_marks)

    for i in range(len(list_marks)):
        if list_marks[i] == max_elem:
            list_marks[i] = min_elem

    return list_marks


for mark in change_marks():
    print(mark, end=' ')
