# Задача №54. Простой стек
# https://informatics.mccme.ru/mod/statements/view3.php?id=207&chapterid=54#1



class SimpleStack:
    def __init__(self):
        self.list_numbers = []

    def push(self, number):
        self.list_numbers.append(number)
        return 'ok'

    def pop(self):
        return self.list_numbers.pop()

    def back(self):
        return self.list_numbers[-1]

    def size(self):
        return len(self.list_numbers)

    def clear(self):
        self.list_numbers = []
        return 'ok'


if __name__ == '__main__':
    command = input().split()
    simple_stack = SimpleStack()

    while 'exit' not in command:
        if command[0] == 'push':
            print(simple_stack.push(int(command[1])))

        elif command[0] == 'size':
            print(simple_stack.size())

        elif command[0] == 'pop':
            print(simple_stack.pop())

        elif command[0] == 'back':
            print(simple_stack.back())

        elif command[0] == 'clear':
            print(simple_stack.clear())

        command = input().split()

    print('bye')



