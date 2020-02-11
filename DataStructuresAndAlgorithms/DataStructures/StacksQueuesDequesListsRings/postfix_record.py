class UnlimitedStack:
    def __init__(self):
        self.list_elements = [None] * 10
        self.start_position = self.end_position = 0

    def push(self, element):
        self.stack_overflow_check()
        self.list_elements[self.end_position] = element
        self.end_position += 1
        return 'ok'

    def stack_overflow_check(self):
        if self.end_position == len(self.list_elements):
            self.list_elements.extend([None] * 10)

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
        self.list_elements = [None] * 10
        self.start_position = self.end_position = 0
        return 'ok'

    def main_program(self, symbol):
        if symbol.isdigit():
            self.push(int(symbol))

        else:
            last_element = self.pop()
            penultimate_element = self.pop()
            if symbol == '+':
                self.push(last_element + penultimate_element)

            elif symbol == '-':
                self.push(penultimate_element - last_element)

            elif symbol == '*':
                self.push(last_element * penultimate_element)


if __name__ == '__main__':

    stack = UnlimitedStack()
    sequence = input().split()
    for character in sequence:
        stack.main_program(character)

    # print(stack.is_correct_bracket_sequence())
    print(stack.list_elements[stack.start_position])


