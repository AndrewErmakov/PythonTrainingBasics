# Задача №60. Простой дек
# https://informatics.mccme.ru/mod/statements/view3.php?id=207&chapterid=60#1


class SimpleDeque:
    def __init__(self):
        self.deque = []
        self.size = 0

    def push_back(self, number):
        self.deque.append(number)
        self.size += 1
        return 'ok'

    def push_front(self, number):
        self.deque = [number] + self.deque
        self.size += 1
        return 'ok'

    def pop_front(self):
        element = self.deque[0]
        self.deque = self.deque[1:]
        self.size -= 1
        return element

    def pop_back(self):
        element = self.deque[-1]
        self.deque = self.deque[:-1]
        self.size -= 1
        return element

    def front(self):
        return self.deque[0]

    def back(self):
        return self.deque[-1]

    def size_deque(self):
        return self.size

    def clear(self):
        self.deque = []
        self.size = 0
        return 'ok'


if __name__ == '__main__':
    deque = SimpleDeque()
    command = input().split()
    while 'exit' not in command:
        if command[0] == 'push_front':
            print(deque.push_front(int(command[1])))

        if command[0] == 'push_back':
            print(deque.push_back(int(command[1])))

        if command[0] == 'pop_front':
            print(deque.pop_front())

        if command[0] == 'pop_back':
            print(deque.pop_back())

        if command[0] == 'front':
            print(deque.front())

        if command[0] == 'back':
            print(deque.back())

        if command[0] == 'size':
            print(deque.size_deque())

        if command[0] == 'clear':
            print(deque.clear())

        command = input().split()

    print('bye')
