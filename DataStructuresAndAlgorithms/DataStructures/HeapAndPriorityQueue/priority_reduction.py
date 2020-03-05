# Задача №1165. Уменьшение приоритета
# https://informatics.mccme.ru/mod/statements/view3.php?id=1234&chapterid=1165#1


class SimpleHeap:
    def __init__(self, heap_elements, count_elements):
        self.heap_elements = heap_elements
        self.size_heap = count_elements

    def presence_left_child(self, i):
        return 2 * i + 1 < self.size_heap

    def presence_right_child(self, right_child):
        return right_child < self.size_heap

    def sift_down(self, position):
        while self.presence_left_child(position):
            left_child = 2 * position + 1
            right_child = 2 * position + 2
            child_index = left_child
            if self.presence_right_child(right_child) and self.heap_elements[right_child] > self.heap_elements[left_child]:
                child_index = right_child

            if self.heap_elements[position] >= self.heap_elements[child_index]:
                break
            self.heap_elements[position], self.heap_elements[child_index] = \
                self.heap_elements[child_index], self.heap_elements[position]

            position = child_index

        return position + 1

    def main(self, variable_element_index, order_magnification):
        self.heap_elements[variable_element_index - 1] -= order_magnification
        return self.sift_down(variable_element_index - 1)


if __name__ == '__main__':
    number_elements = int(input())

    elements = [int(i) for i in input().split()]
    heap = SimpleHeap(elements, number_elements)

    count_requests = int(input())
    for _ in range(count_requests):
        index, number = map(int, input().split())
        print(heap.main(index, number))

    for elem in heap.heap_elements:
        print(elem, end=' ')


