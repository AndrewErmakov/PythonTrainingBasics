# Задача №51. Правильная скобочная последовательность
# https://informatics.mccme.ru/mod/statements/view3.php?id=206&chapterid=51#1


class UnlimitedStack:
    def __init__(self):
        self.list_elements = [None] * 1000
        self.start_position = self.end_position = 0

    def push(self, element):
        self.stack_overflow_check()
        self.list_elements[self.end_position] = element
        self.end_position += 1
        return 'ok'

    def stack_overflow_check(self):
        if self.end_position == len(self.list_elements):
            self.list_elements.extend([None] * 1000)

    def is_stack_empty(self):
        return self.start_position == self.end_position

    def pop(self):
        if self.is_stack_empty():
            return 'error'
        else:
            last_element = self.list_elements[self.end_position - 1]
            self.list_elements[self.end_position - 1] = None
            self.end_position -= 1
            return last_element

    def back(self):
        if self.is_stack_empty():
            return 'error'
        else:
            return self.list_elements[self.end_position - 1]

    def size(self):
        return self.end_position - self.start_position

    def clear(self):
        self.list_elements = [None] * 1000
        self.start_position = self.end_position = 0
        return 'ok'

    def main_program(self, symbol):
        if symbol in '([{' or self.size() == 0:
            self.push(symbol)

        else:
            last_opening_bracket = self.back()
            self.push(symbol)
            if (ord(symbol) < 50 > ord(last_opening_bracket) and ord(symbol) - ord(last_opening_bracket) == 1) \
                    or (ord(symbol) > 50 < ord(last_opening_bracket) and ord(symbol) - ord(last_opening_bracket) == 2):
                for i in range(2):
                    self.pop()

    def is_correct_bracket_sequence(self):
        if self.size() == 0:
            return 'yes'
        else:
            return 'no'


if __name__ == '__main__':

    stack = UnlimitedStack()
    sequence = input()
    for bracket in sequence:
        stack.main_program(bracket)

    print(stack.is_correct_bracket_sequence())



