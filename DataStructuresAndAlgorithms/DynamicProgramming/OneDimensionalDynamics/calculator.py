# Задача №2963. Калькулятор
# https://www.informatics.mccme.ru/mod/statements/view3.php?id=654&chapterid=2963#1


class Calculator:
    def __init__(self):
        self.count_operations = [None] * 1000000

    def definition_basic_case(self):
        # Number of operations to get from 1 number 1
        self.count_operations[0] = 0

    def calculate(self, num):
        for i in range(1, num):
            # the numbers for which we got the number N
            intermediate_states = [self.count_operations[i - 1]]
            if (i + 1) % 2 == 0:
                intermediate_states.append(self.count_operations[i // 2])
            if (i + 1) % 3 == 0:
                intermediate_states.append(self.count_operations[i // 3])

            self.count_operations[i] = 1 + min(intermediate_states)

        return self.count_operations[num - 1]


if __name__ == '__main__':
    number = int(input())
    calculator = Calculator()
    calculator.definition_basic_case()
    print(calculator.calculate(number))
