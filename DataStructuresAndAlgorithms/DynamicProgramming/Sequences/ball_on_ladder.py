# Задача №203. Мячик на лесенке
# https://informatics.mccme.ru/mod/statements/view3.php?id=649&chapterid=203#1


class FibonacciNumbers:
    def __init__(self):
        self.fibonacci_numbers = [None] * 32

    def set_initial_states(self):
        self.fibonacci_numbers[0] = 1
        self.fibonacci_numbers[1] = 2
        self.fibonacci_numbers[2] = 4

    def get_fibonacci_number(self, num):
        for i in range(3, num):
            self.fibonacci_numbers[i] = self.fibonacci_numbers[i - 1] + self.fibonacci_numbers[i - 2] \
                                        + self.fibonacci_numbers[i - 3]
        return self.fibonacci_numbers[num - 1]


if __name__ == '__main__':
    number = int(input())
    fibonacci = FibonacciNumbers()
    fibonacci.set_initial_states()
    print(fibonacci.get_fibonacci_number(number))

