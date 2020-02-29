# Задача №1164. Увеличение приоритета
# https://informatics.mccme.ru/mod/statements/view.php?id=1234#1


class VerySimpleHeap:
    def __init__(self, head_elements):
        self.heap_elements = head_elements

    def sift_up(self, pos):
        if not self.is_empty_heap():
            while self.heap_elements[pos] > self.heap_elements[(pos - 1) // 2] and pos > 0:
                self.heap_elements[pos], self.heap_elements[(pos - 1) // 2] = self.heap_elements[(pos - 1) // 2], \
                                                                              self.heap_elements[pos]
                pos = (pos - 1) // 2

        return pos + 1

    def main(self, variable_element_index, order_magnification):
        self.heap_elements[variable_element_index - 1] += order_magnification
        return self.sift_up(variable_element_index - 1)

    def is_empty_heap(self):
        return len(self.heap_elements) == 0


if __name__ == '__main__':
    number_elements = int(input())

    elements = [int(i) for i in input().split()]
    heap = VerySimpleHeap(elements)

    count_requests = int(input())
    for _ in range(count_requests):
        index, number = map(int, input().split())
        print(heap.main(index, number))

    for elem in heap.heap_elements:
        print(elem, end=' ')


