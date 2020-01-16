import sys

coordinate_x = coordinate_y = 0
for line in sys.stdin:
    description = line.split()
    if description[0] == "South":
        coordinate_y -= int(description[1])

    elif description[0] == "North":
        coordinate_y += int(description[1])

    elif description[0] == "East":
        coordinate_x += int(description[1])

    else:
        coordinate_x -= int(description[1])


print(coordinate_x, coordinate_y)


