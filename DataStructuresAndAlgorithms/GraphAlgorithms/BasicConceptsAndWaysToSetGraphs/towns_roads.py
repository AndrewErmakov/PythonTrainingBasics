# https://www.informatics.mccme.ru/mod/statements/view.php?id=259#1
# Задача №174. Города и дороги


class Roads:
    def __init__(self, count_towns):
        self.count_towns = count_towns
        self.roads = []
        self.count_roads = 0

    def determination_number_roads(self):
        for i in range(self.count_towns):
            for j in range(self.count_towns):
                if self.roads[i][j] == 1:
                    self.count_roads += 1

        self.count_roads //= 2
        return self.count_roads


if __name__ == '__main__':
    number_towns = int(input())
    network_towns = Roads(number_towns)

    for i in range(number_towns):
        network_towns.roads.append([int(i) for i in input().split()])

    number_roads = network_towns.determination_number_roads()
    print(number_roads)
