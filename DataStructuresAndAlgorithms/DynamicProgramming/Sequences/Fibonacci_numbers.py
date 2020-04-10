# Задача №201. Числа Фибоначи
# https://informatics.mccme.ru/mod/statements/view.php?id=649#1


class FibonacciNumbers:
    def __init__(self):
        self.fibonacci_numbers = [None] * 45

    def set_initial_states(self):
        self.fibonacci_numbers[0] = self.fibonacci_numbers[1] = 1

    def get_fibonacci_number(self, num):
        for i in range(2, num):
            self.fibonacci_numbers[i] = self.fibonacci_numbers[i - 1] + self.fibonacci_numbers[i - 2]
        return self.fibonacci_numbers[num - 1]


if __name__ == '__main__':
    number = int(input())
    fibonacci = FibonacciNumbers()
    fibonacci.set_initial_states()
    print(fibonacci.get_fibonacci_number(number))

