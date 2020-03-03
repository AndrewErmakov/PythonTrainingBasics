# Задача №1167. Приоритетная очередь
# https://informatics.mccme.ru/mod/statements/view3.php?id=1234&chapterid=1167#1


class PriorityQueue:
    def __init__(self, max_size):
        self.start = 0
        self.finish = 0
        self.max_size = max_size
        self.heap_elements = [None] * self.max_size

    def size_heap(self):
        """
        Function for determining the current heap size
        :return: Integer Heap Size
        """
        return self.finish - self.start

    def is_empty_heap(self):
        """
        The condition under which the heap is empty
        :return: True or False
        """
        return self.size_heap() == 0

    def is_full_heap(self):
        """
        The condition under which the heap is full
        :return: True or False
        """
        return self.size_heap() == self.max_size

    def sift_up(self, pos):
        if not self.is_empty_heap():
            while self.heap_elements[pos] > self.heap_elements[(pos - 1) // 2]:
                self.heap_elements[pos], self.heap_elements[(pos - 1) // 2] = self.heap_elements[(pos - 1) // 2], \
                                                                              self.heap_elements[pos]
                pos = (pos - 1) // 2

                if pos == 0:
                    break

        return pos + 1

    def insert(self, new_element):
        if self.is_full_heap():
            return -1
        else:
            self.heap_elements[self.finish] = new_element
            self.finish += 1
            if self.size_heap() > 1:
                return self.sift_up(self.finish - 1)

            else:
                return self.finish

    def condition_absence_ancestors(self, position):
        """
        Condition under which the current node has no children
        :return: True or False
        """
        return 2 * position + 1 >= self.size_heap() and 2 * position + 2 >= self.size_heap()

    def conditions_presence_one_descendant(self, position):
        """
        Condition in which the current node has only one child
        :return: True or False
        """
        return 2 * position + 1 < self.size_heap() <= 2 * position + 2

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

    def extract_max(self):
        """
        Retrieves the maximum item from the heap.
        The last element of the heap is placed in place of the maximum element,
        then this element is sifted down as necessary.
        :return: 1. -1 if the heap is empty
                 2. the value of the maximum element and the new position (index) of the sifted element
                 3. 0 if the last item is retrieved on the heap
        """
        if self.is_empty_heap():
            return -1
        else:
            max_elem = self.heap_elements[0]
            self.heap_elements[0] = self.heap_elements[self.finish - 1]
            self.finish -= 1

            new_position = self.sift_down(pos=0) if self.finish != 0 else 0

            return new_position, max_elem

    def main_program(self, instruction):
        if instruction[0] == '1':
            return self.extract_max()
        elif instruction[0] == '2':
            return self.insert(int(instruction[1]))


if __name__ == '__main__':

    max_heap_size, count_requests = map(int, input().split())
    heap = PriorityQueue(max_heap_size)

    for i in range(count_requests):
        request = input().split()
        result = heap.main_program(request)
        if type(result) != tuple:
            print(result)
        else:
            for chunk in result:
                print(chunk, end=' ')
            print()
    if heap.size_heap() != 0:
        for element in heap.heap_elements[heap.start:heap.finish]:
            print(element, end=' ')

