# Задача №58. Очередь с защитой от ошибок
# https://informatics.mccme.ru/mod/statements/view3.php?id=207&chapterid=58#1


SIZE_QUEUE = 100000


class SimpleQueue:
    def __init__(self):
        self.list_numbers = [None] * SIZE_QUEUE
        self.start = self.finish = 0

    def push(self, number):
        self.list_numbers[self.finish] = number
        self.finish += 1
        return 'ok'

    def pop(self):
        if self.is_queue_empty():
            return 'error'
        else:
            first_elem = self.list_numbers[self.start]
            self.start += 1
            return first_elem

    def front(self):
        if self.is_queue_empty():
            return 'error'
        else:
            return self.list_numbers[self.start]

    def size(self):
        return self.finish - self.start

    def is_queue_empty(self):
        return self.start == self.finish

    def clear(self):
        self.start = self.finish = 0
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
