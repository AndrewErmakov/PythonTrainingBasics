number_people = int(input())

set_scores = set([int(i) for i in input().split()])

second_max = max(set_scores.difference({max(set_scores)}))

print(second_max)
