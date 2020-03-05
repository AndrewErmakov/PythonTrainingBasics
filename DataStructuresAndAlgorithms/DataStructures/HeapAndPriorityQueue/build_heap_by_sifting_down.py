# Задача №1170. Построение кучи просеиванием вниз
# https://informatics.mccme.ru/mod/statements/view3.php?id=1234&chapterid=1170#1


class BuildHeap:
    def __init__(self, size_heap, list_elements):
        self.heap_elements = list_elements
        self.size_heap = size_heap

    def presence_left_child(self, i):
        """
        the function of determining whether this node has at least one child (left)
        :param i: index of current node
        :return: 1. True if the left child is
                 2. False if the left child is not
        """
        return 2 * i + 1 < self.size_heap

    def presence_right_child(self, right_child):
        """
        function for determining whether a node has a right child in a heap
        :param right_child: formal legal child index
        :return: 1. True if the right child is
                 2. False if the right child is not
        """
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

    def main_program(self):
        for i in range(self.size_heap // 2, -1, -1):
            self.sift_down(i)


if __name__ == '__main__':
    count_elements = int(input())
    elements = [int(i) for i in input().split()]
    build_heap = BuildHeap(count_elements, elements)
    build_heap.main_program()
    for i in range(count_elements):
        print(build_heap.heap_elements[i], end=' ')


