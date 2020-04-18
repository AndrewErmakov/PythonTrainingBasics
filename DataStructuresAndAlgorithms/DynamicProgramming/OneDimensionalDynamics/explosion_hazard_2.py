# Задача №914. Взрывоопасность-2
# https://www.informatics.mccme.ru/mod/statements/view3.php?id=654&chapterid=914#1


class Sequence:
    def __init__(self):
        self.size_sequence = 20

        # the number of formed stacks with type A is first indicated in the zero index
        # the number of formed stacks with type B is first indicated in the first index
        # the number of formed stacks with type C is first indicated in the second index

        self.sequence = []
        for i in range(self.size_sequence):
            self.sequence.append([])

    def definition_basic_cases(self):

        # number of container sequences of unit length
        for i in range(3):
            self.sequence[0].append(1)

        # number of container sequences of length 2
        for i in range(3):
            if i == 0:
                self.sequence[1].append(2)
            else:
                self.sequence[1].append(3)

    def determination_length_container_sequences(self, num: int) -> int:
        for i in range(2, num):
            self.sequence[i].append(self.sequence[i - 1][1] + self.sequence[i - 1][2])
            for _ in range(2):
                self.sequence[i].append(self.sequence[i - 1][0] + self.sequence[i - 1][1] + self.sequence[i - 1][2])

        return sum(self.sequence[num - 1])


if __name__ == '__main__':
    sequence = Sequence()
    sequence.definition_basic_cases()
    len_sequence = int(input())
    print(sequence.determination_length_container_sequences(len_sequence))
