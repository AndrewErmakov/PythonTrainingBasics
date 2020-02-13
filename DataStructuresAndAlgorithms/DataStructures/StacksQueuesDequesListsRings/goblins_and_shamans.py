# Задача №112984. Гоблины и шаманы
# https://informatics.mccme.ru/mod/statements/view3.php?id=206&chapterid=112984#1


from math import ceil

SIZE_QUEUE = 200000


class UnlimitedQueue:
    def __init__(self):
        self.list_numbers = [None] * SIZE_QUEUE
        self.start = self.finish = 0
        self.max_size_queue = SIZE_QUEUE
        self.cured_numbers_goblins = []

    def push(self, number):
        if self.check_stack_overflow():
            self.list_numbers += [None] * self.max_size_queue
            self.max_size_queue *= 2

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

    def check_stack_overflow(self):
        return self.max_size_queue == self.finish

    def main_program(self, instruction):
        if instruction[0] == '+':
            self.push(int(instruction[1]))

        elif instruction[0] == '*':
            median_index = ceil((self.start + self.finish) / 2)
            second_half_queue = self.list_numbers[median_index:self.finish]
            self.list_numbers[median_index] = int(instruction[1])
            self.finish += 1
            self.list_numbers[median_index + 1:self.finish] = second_half_queue

        elif instruction[0] == '-':
            self.cured_numbers_goblins.append(self.pop())


if __name__ == '__main__':
    number_commands = int(input())
    queue = UnlimitedQueue()
    for i in range(number_commands):
        command = input().split()
        queue.main_program(command)

    for i in range(len(queue.cured_numbers_goblins)):
        print(queue.cured_numbers_goblins[i])


