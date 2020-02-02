# Задача №56. Стек неограниченного размера
# https://informatics.mccme.ru/mod/statements/view3.php?id=207&chapterid=56#1


class UnlimitedStack:
    def __init__(self):
        self.list_numbers = [None] * 1000
        self.start_position = self.end_position = 0

    def push(self, number):
        self.stack_overflow_check()
        self.list_numbers[self.end_position] = number
        self.end_position += 1
        return 'ok'

    def stack_overflow_check(self):
        if self.end_position == 1000:
            self.list_numbers.extend([None] * 1000)

    def is_stack_empty(self):
        return self.start_position == self.end_position

    def pop(self):
        if self.is_stack_empty():
            return 'error'
        else:
            last_number = self.list_numbers[self.end_position - 1]
            self.list_numbers[self.end_position - 1] = None
            self.end_position -= 1
            return last_number

    def back(self):
        if self.is_stack_empty():
            return 'error'
        else:
            return self.list_numbers[self.end_position - 1]

    def size(self):
        return self.end_position - self.start_position

    def clear(self):
        self.list_numbers = [None] * 1000
        self.start_position = self.end_position = 0
        return 'ok'


if __name__ == '__main__':
    stack = UnlimitedStack()
    command = input().split()

    while 'exit' not in command:
        if command[0] == 'push':
            print(stack.push(int(command[1])))

        elif command[0] == 'size':
            print(stack.size())

        elif command[0] == 'pop':
            print(stack.pop())

        elif command[0] == 'back':
            print(stack.back())

        elif command[0] == 'clear':
            print(stack.clear())

        command = input().split()

    print('bye')

