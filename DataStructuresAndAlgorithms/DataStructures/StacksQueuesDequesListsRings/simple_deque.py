# Задача №60. Простой дек
# https://informatics.mccme.ru/mod/statements/view3.php?id=207&chapterid=60#1


class SimpleDeque:
    def __init__(self):
        self.deque = [None] * 300
        self.start = self.end = 150

    def push_back(self, number):
        self.deque[self.end] = number
        self.end += 1
        return 'ok'

    def push_front(self, number):
        self.start -= 1
        self.deque[self.start] = number
        return 'ok'

    def pop_front(self):
        element = self.deque[self.start]
        self.start += 1
        return element

    def pop_back(self):
        element = self.deque[self.end - 1]
        self.end -= 1
        return element

    def front(self):
        return self.deque[self.start]

    def back(self):
        return self.deque[self.end - 1]

    def size_deque(self):
        return self.end - self.start

    def clear(self):
        self.start = self.end = 150
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

