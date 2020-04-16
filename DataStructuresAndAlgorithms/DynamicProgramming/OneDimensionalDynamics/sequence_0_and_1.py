# Задача №207. Последовательность из 0 и 1
# https://www.informatics.mccme.ru/mod/statements/view.php?id=654#1


class Sequence:
    def __init__(self):
        self.size_sequence = 100
        self.sequence = [None] * self.size_sequence

    def definition_basic_cases(self):
        # number of sequences of unit length
        self.sequence[0] = 2
        # number of sequences of length equal to 2
        self.sequence[1] = 3

    def determination_length_sequences(self, num: int) -> int:
        for i in range(2, num):
            self.sequence[i] = self.sequence[i - 2] + self.sequence[i - 1]

        return self.sequence[num - 1]


if __name__ == '__main__':
    sequence = Sequence()
    sequence.definition_basic_cases()
    len_sequence = int(input())
    print(sequence.determination_length_sequences(len_sequence))
