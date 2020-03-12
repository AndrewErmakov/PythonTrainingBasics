# Задача №1171. Пирамидальная сортировка - подробно
# https://informatics.mccme.ru/mod/statements/view3.php?id=1234&chapterid=1171#1


class SortByHeap:
    def __init__(self, list_elements, size):
        self.heap_elements = list_elements
        self.size_heap = size

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
            if self.presence_right_child(right_child) and self.heap_elements[right_child] > \
                    self.heap_elements[left_child]:
                child_index = right_child

            if self.heap_elements[position] >= self.heap_elements[child_index]:
                break

            self.heap_elements[position], self.heap_elements[child_index] = \
                self.heap_elements[child_index], self.heap_elements[position]

            position = child_index

        return position + 1

    def build_heap(self):
        for i in range(self.size_heap // 2, -1, -1):
            self.sift_down(i)
        return self.heap_elements[:self.size_heap]

    def modernized_extract_max(self):
        self.heap_elements[0], self.heap_elements[self.size_heap - 1] = self.heap_elements[self.size_heap - 1], \
                                                                        self.heap_elements[0]
        self.size_heap -= 1

    def getting_state_pyramidal_sort(self):
        intermediate_result_heap = self.build_heap()
        self.modernized_extract_max()
        return intermediate_result_heap


if __name__ == '__main__':
    count_elements = int(input())
    elements = [int(i) for i in input().split()]
    sorting = SortByHeap(elements, count_elements)

    for i in range(count_elements):
        for element in sorting.getting_state_pyramidal_sort():
            print(element, end=' ')
        print()

    for i in range(count_elements):
        print(sorting.heap_elements[i], end=' ')
