# Задача №3086. Разложение в сумму кубов
# https://www.informatics.mccme.ru/mod/statements/view.php?id=813#1
from math import ceil


class NumberExpansion:
    def __init__(self, num):
        self.possible_terms = []
        self.num = num
        self.count_terms = 0

    def definition_possible_terms(self):
        max_possible_term = int(self.num ** (1 / 3))
        for i in range(1, max_possible_term + 1):
            self.possible_terms.append(i)

    def find_exact_cubes(self):
        # min_counters
        count_possible_terms = len(self.possible_terms)
        for i in range(-1, -count_possible_terms - 1, -1):
            flag_term = False

            while self.num >= self.possible_terms[i] ** 3:
                self.num -= self.possible_terms[i] ** 3

                if self.num == 0:
                    break

            if flag_term is True:
                self.count_terms += 1

        return self.count_terms
if __name__ == '__main__':
    number = int(input())
    number_expansion = NumberExpansion(number)
    number_expansion.definition_possible_terms()

    print(number_expansion.find_exact_cubes())
