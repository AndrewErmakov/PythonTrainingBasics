# Задача №1166. Извлечение максимального
# https://informatics.mccme.ru/mod/statements/view3.php?id=1234&chapterid=1166#1


class Heap:
    def __init__(self, heap_elements, count_elements):
        self.heap_elements = heap_elements
        self.size_heap = count_elements

    def condition_absence_ancestors(self, position):
        """
        Condition under which the current node has no children
        :return: True or False
        """
        return 2 * position + 1 >= self.size_heap and 2 * position + 2 >= self.size_heap

    def conditions_presence_one_descendant(self, position):
        """
        Condition in which the current node has only one descendant
        :return: True or False
        """
        return 2 * position + 1 < self.size_heap <= 2 * position + 2

    def sift_down(self, pos):
        flag = True
        while flag and not self.condition_absence_ancestors(pos):
            if not self.conditions_presence_one_descendant(pos):
                if self.heap_elements[pos] < self.heap_elements[2 * pos + 1] and self.heap_elements[2 * pos + 1] >= \
                        self.heap_elements[2 * pos + 2]:
                    self.heap_elements[pos], self.heap_elements[2 * pos + 1] = self.heap_elements[2 * pos + 1], \
                                                                               self.heap_elements[pos]
                    pos = 2 * pos + 1

                elif self.heap_elements[pos] < self.heap_elements[2 * pos + 2] and self.heap_elements[2 * pos + 2] >= \
                        self.heap_elements[2 * pos + 1]:
                    self.heap_elements[pos], self.heap_elements[2 * pos + 2] = self.heap_elements[2 * pos + 2], \
                                                                               self.heap_elements[pos]
                    pos = 2 * pos + 2

                else:
                    flag = False

            else:
                if self.heap_elements[pos] < self.heap_elements[2 * pos + 1]:
                    self.heap_elements[pos], self.heap_elements[2 * pos + 1] = self.heap_elements[2 * pos + 1], \
                                                                               self.heap_elements[pos]
                    pos = 2 * pos + 1
                else:
                    flag = False

        return pos + 1

    def is_empty_heap(self):
        return self.size_heap == 0

    def extract_max(self):
        max_elem = self.heap_elements[0]
        self.heap_elements[0] = self.heap_elements[self.size_heap - 1]
        self.size_heap -= 1
        new_position = self.sift_down(pos=0)
        return new_position, max_elem

    def main(self):
        return self.extract_max()


if __name__ == '__main__':
    number_elements = int(input())

    elements = [int(i) for i in input().split()]
    heap = Heap(elements, number_elements)
    while heap.size_heap > 1:
        data = heap.main()

        for chunk in data:
            print(chunk, end=' ')
        print()

