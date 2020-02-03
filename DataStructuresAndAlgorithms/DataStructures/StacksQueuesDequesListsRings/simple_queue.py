# Задача №57. Простая очередь
# https://informatics.mccme.ru/mod/statements/view3.php?id=207&chapterid=57#1


class SimpleQueue:
    def __init__(self):
        self.list_numbers = []
        self.start_position = self.end_position = 0

    def push(self, number):
        self.list_numbers.append(number)
        self.end_position += 1
        return 'ok'

    def pop(self):
        element = self.list_numbers[0]
        self.list_numbers = self.list_numbers[1:]
        self.end_position -= 1
        return element

    def front(self):
        return self.list_numbers[0]

    def size(self):
        return self.end_position

    def clear(self):
        self.list_numbers = []
        self.start_position = self.end_position = 0
        return 'ok'


if __name__ == '__main__':
    command = input().split()
    queue = SimpleQueue()
    while 'exit' not in command:
        if command[0] == 'push':
            print(queue.push(int(command[1])))

        elif command[0] == 'size':
            print(queue.size())

        elif command[0] == 'pop':
            print(queue.pop())

        elif command[0] == 'front':
            print(queue.front())

        elif command[0] == 'clear':
            print(queue.clear())

        command = input().split()

    print('bye')


