# Задача №1169. Построение кучи просеиванием вверх
# https://informatics.mccme.ru/mod/statements/view3.php?id=1234&chapterid=1169#1


class BuildHeap:
    def __init__(self, size_heap):
        self.heap_elements = [None] * size_heap
        self.finish = 0

    def size_heap(self):
        """
        Function for determining the current heap size
        :return: Integer Heap Size
        """
        return self.finish

    def is_empty_heap(self):
        """
        The condition under which the heap is empty
        :return: True or False
        """
        return self.size_heap() == 0

    def sift_up(self, pos):
        if not self.is_empty_heap():
            while self.heap_elements[pos] > self.heap_elements[(pos - 1) // 2]:
                self.heap_elements[pos], self.heap_elements[(pos - 1) // 2] = self.heap_elements[(pos - 1) // 2], \
                                                                              self.heap_elements[pos]
                pos = (pos - 1) // 2

                if pos == 0:
                    break

        return pos + 1

    def main_program(self, new_element):
        self.heap_elements[self.finish] = new_element
        self.finish += 1
        if self.size_heap() > 1:
            self.sift_up(self.finish - 1)


if __name__ == '__main__':
    count_elements = int(input())
    create_heap = BuildHeap(count_elements)
    list_elements = [int(i) for i in input().split()]

    for i in range(count_elements):
        create_heap.main_program(list_elements[i])

    for i in range(count_elements):
        print(create_heap.heap_elements[i], end=' ')

