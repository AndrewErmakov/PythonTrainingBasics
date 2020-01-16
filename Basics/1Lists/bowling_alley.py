pins_number, balls_number = [int(s) for s in input().split()]
bowling_alley = ['I'] * pins_number
for i in range(balls_number):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bowling_alley[j] = '.'

for elem in bowling_alley:
    print(elem, end='')
	
