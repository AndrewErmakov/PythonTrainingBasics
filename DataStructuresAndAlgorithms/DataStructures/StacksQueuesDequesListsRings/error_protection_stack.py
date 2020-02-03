# Задача №55. Стек с защитой от ошибок
# https://informatics.mccme.ru/mod/statements/view3.php?id=207&chapterid=55#1



class ErrorProtectionStack:
    def __init__(self):
        self.list_numbers = []

    def push(self, number):
        self.list_numbers.append(number)
        return 'ok'

    def pop(self):
        if self.size() == 0:
            return 'error'
        else:
            return self.list_numbers.pop()

    def back(self):
        if self.size() == 0:
            return 'error'
        else:
            return self.list_numbers[-1]

    def size(self):
        return len(self.list_numbers)

    def clear(self):
        self.list_numbers = []
        return 'ok'


if __name__ == '__main__':
    command = input().split()
    stack = ErrorProtectionStack()

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





