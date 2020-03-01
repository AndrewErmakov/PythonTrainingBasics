# Задача №1165. Уменьшение приоритета
# https://informatics.mccme.ru/mod/statements/view3.php?id=1234&chapterid=1165#1


class SimpleHeap:
    def __init__(self, heap_elements):
        self.heap_elements = heap_elements
        self.size_heap = len(self.heap_elements)
        # self.max_level = int(log2(self.size_heap))

    def is_empty_heap(self):
        return len(self.heap_elements) == 0

    def condition_absence_ancestors(self, position):
        return 2 * position + 1 >= self.size_heap and 2 * position + 2 >= self.size_heap

    def conditions_presence_one_descendant(self, position):
        return 2 * position + 1 < self.size_heap <= 2 * position + 2

    def sift_down(self, pos):
        # current_level = int(log2(pos + 1))
        flag = True
        while flag and not self.condition_absence_ancestors(pos):
            if not self.conditions_presence_one_descendant(pos):
                if self.heap_elements[pos] < self.heap_elements[2*pos + 1] and self.heap_elements[2*pos + 1] >= \
                        self.heap_elements[2 * pos + 2]:
                    self.heap_elements[pos], self.heap_elements[2 * pos + 1] = self.heap_elements[2*pos + 1], \
                                                                               self.heap_elements[pos]
                    pos = 2 * pos + 1
                    # current_level += 1

                elif self.heap_elements[pos] < self.heap_elements[2*pos + 2] and self.heap_elements[2*pos + 2] >= \
                        self.heap_elements[2*pos + 1]:
                    self.heap_elements[pos], self.heap_elements[2*pos + 2] = self.heap_elements[2*pos + 2], \
                                                                               self.heap_elements[pos]
                    pos = 2 * pos + 2
                    # current_level += 1

                else:
                    flag = False

            else:
                if self.heap_elements[pos] < self.heap_elements[2*pos + 1]:
                    self.heap_elements[pos], self.heap_elements[2*pos + 1] = self.heap_elements[2*pos + 1], \
                                                                               self.heap_elements[pos]
                    pos = 2 * pos + 1
                else:
                    flag = False

        return pos + 1

    def main(self, variable_element_index, order_magnification):
        self.heap_elements[variable_element_index - 1] -= order_magnification
        return self.sift_down(variable_element_index - 1)


if __name__ == '__main__':
    number_elements = int(input())

    elements = [int(i) for i in input().split()]
    heap = SimpleHeap(elements)

    count_requests = int(input())
    for _ in range(count_requests):
        index, number = map(int, input().split())
        print(heap.main(index, number))

    for elem in heap.heap_elements:
        print(elem, end=' ')
