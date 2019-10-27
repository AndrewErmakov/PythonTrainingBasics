num_states = int(input())

dict_votes = dict()


for i in range(num_states):
    name_president, num_votes_in_state = input().split()
    if name_president not in dict_votes:
        dict_votes[name_president] = int(num_votes_in_state)

    else:
        dict_votes[name_president] += int(num_votes_in_state)

for key, value in sorted(dict_votes.items()):
    print(key, value)

