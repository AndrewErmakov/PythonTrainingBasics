# Задача №61. Дек с защитой от ошибок
# https://informatics.mccme.ru/mod/statements/view3.php?id=207&chapterid=61#1


class ErrorProtectionDeque:
    def __init__(self):
        self.deque = [None] * 3000
        self.start = self.end = 1500

    def push_back(self, number):
        self.deque[self.end] = number
        self.end += 1
        self.check()
        return 'ok'

    def push_front(self, number):
        self.start -= 1
        self.deque[self.start] = number
        self.check()
        return 'ok'

    def pop_front(self):
        if self.is_deque_empty():
            return 'error'
        else:
            element = self.deque[self.start]
            self.start += 1
            self.check()
            return element

    def pop_back(self):
        if self.is_deque_empty():
            return 'error'
        else:
            element = self.deque[self.end - 1]
            self.end -= 1
            self.check()
            return element

    def front(self):
        if self.is_deque_empty():
            return 'error'
        else:
            return self.deque[self.start]

    def back(self):
        if self.is_deque_empty():
            return 'error'
        else:
            return self.deque[self.end - 1]

    def size_deque(self):
        if self.end < self.start:
            return len(self.deque) - self.start + self.end
        else:
            return self.end - self.start

    def clear(self):
        self.start = self.end = 1500
        return 'ok'

    def is_deque_empty(self):
        # return self.end - self.start == 0
        return self.size_deque() == 0

    def check(self):
        if self.start < 0:
            self.start += len(self.deque)
        if self.end < 0:
            self.end += len(self.deque)

        if self.start >= len(self.deque):
            self.start -= len(self.deque)

        if self.end >= len(self.deque):
            self.end -= len(self.deque)


if __name__ == '__main__':
    deque = ErrorProtectionDeque()
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



