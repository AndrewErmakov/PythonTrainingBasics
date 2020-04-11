# Задача №843. Простая последовательность
# https://informatics.mccme.ru/mod/statements/view3.php?id=649&chapterid=843#1


class SimpleSequence:
    def __init__(self):
        self.sequence = [None] * 1001
        self.sequence[0] = self.sequence[1] = 1

    def add_to_sequence(self, num):
        for i in range(2, num + 1):
            if i % 2 == 0:
                self.sequence[i] = self.sequence[i // 2] + self.sequence[i // 2 - 1]
            else:
                self.sequence[i] = self.sequence[i // 2] - self.sequence[i // 2 - 1]

        return self.sequence[num]


if __name__ == '__main__':
    sequence = SimpleSequence()
    number = int(input())
    print(sequence.add_to_sequence(number))
