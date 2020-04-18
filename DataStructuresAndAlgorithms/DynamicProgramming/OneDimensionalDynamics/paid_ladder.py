# Задача №915. Платная лестница
# https://www.informatics.mccme.ru/mod/statements/view3.php?id=654&chapterid=915#1


class Ladder:
    def __init__(self, prices: list, count_stairs: int):
        self.sequence = [None] * 101
        self.prices = prices
        self.count_stairs = count_stairs

    def definition_basic_cases(self):
        self.sequence[0] = self.prices[0]
        if self.count_stairs > 1:
            self.sequence[1] = self.prices[1]

    def determine_cost_climbing_stairs(self):
        for i in range(2, self.count_stairs):
            self.sequence[i] = min(self.sequence[i - 1], self.sequence[i - 2]) + self.prices[i]

        return self.sequence[self.count_stairs - 1]


if __name__ == '__main__':
    number_stairs = int(input())
    price_stairs = [int(i) for i in input().split()]
    ladder = Ladder(price_stairs, number_stairs)
    ladder.definition_basic_cases()
    print(ladder.determine_cost_climbing_stairs())
