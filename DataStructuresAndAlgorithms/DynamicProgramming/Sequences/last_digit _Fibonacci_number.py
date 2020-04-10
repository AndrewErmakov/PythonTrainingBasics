# Задача №842. Последняя цифра числа Фибоначчи
# https://informatics.mccme.ru/mod/statements/view3.php?id=649&chapterid=842#1

class FibonacciNumbers:
    def __init__(self):
        self.fibonacci_numbers = [None] * 1001

    def set_initial_states(self):
        self.fibonacci_numbers[0] = self.fibonacci_numbers[1] = 1

    def get_last_digit_fibonacci_number(self, num):
        for i in range(2, num + 1):
            self.fibonacci_numbers[i] = (self.fibonacci_numbers[i - 1] + self.fibonacci_numbers[i - 2]) % 10
        return self.fibonacci_numbers[num]


if __name__ == '__main__':
    number = int(input())
    fibonacci = FibonacciNumbers()
    fibonacci.set_initial_states()
    print(fibonacci.get_last_digit_fibonacci_number(number))
