# Задача №112984. Гоблины и шаманы
# https://informatics.mccme.ru/mod/statements/view3.php?id=206&chapterid=112984#1

from collections import deque


class GoblinsDeque:
    def __init__(self):
        self.left_part_deque = deque()
        self.right_part_deque = deque()
        self.cured_numbers_goblins = []

    def equilibrium_condition(self):
        return len(self.left_part_deque) == len(self.right_part_deque)

    def push_usual_goblin(self, number):
        if self.equilibrium_condition():
            if len(self.right_part_deque) == 0:
                self.left_part_deque.append(number)
            else:
                self.left_part_deque.append(self.right_part_deque.popleft())
                self.right_part_deque.append(number)
        else:
            self.right_part_deque.append(number)

    def push_authoritative_goblin(self, number):
        if self.equilibrium_condition():
            self.left_part_deque.append(number)

        else:
            self.right_part_deque.appendleft(number)

    def remove_from_queue(self):
        self.cured_numbers_goblins.append(self.left_part_deque.popleft())

        if not self.equilibrium_condition():
            self.left_part_deque.append(self.right_part_deque.popleft())

    def main_program(self, instruction):
        if instruction[0] == '+':
            self.push_usual_goblin(int(instruction[1]))

        elif instruction[0] == '*':
            self.push_authoritative_goblin(int(instruction[1]))

        elif instruction[0] == '-':
            self.remove_from_queue()


if __name__ == '__main__':
    number_commands = int(input())
    queue = GoblinsDeque()
    for i in range(number_commands):
        command = input().split()
        queue.main_program(command)

    for i in range(len(queue.cured_numbers_goblins)):
        print(queue.cured_numbers_goblins[i])




