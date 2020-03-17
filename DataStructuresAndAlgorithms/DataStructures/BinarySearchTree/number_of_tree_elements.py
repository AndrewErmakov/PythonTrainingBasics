# Задача №758. Количество элементов
# https://informatics.mccme.ru/mod/statements/view3.php?id=599&chapterid=758#1


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Node = None
        self.right: Node = None


class BinaryTree:
    def __init__(self):
        self.root: Node = None
        self.count_elements: int = 0

    def add_element(self, x: int):
        if self.root is None:
            self.root: Node = Node(x)
            self.count_elements += 1
            return

        current_node: Node = self.root
        parent_current_node: Node = None

        while current_node is not None:
            parent_current_node = current_node

            if x > current_node.value:
                current_node = current_node.right

            elif x < current_node.value:
                current_node = current_node.left

            else:
                break

        if x > parent_current_node.value:
            parent_current_node.right = Node(x)
            self.count_elements += 1

        elif x < parent_current_node.value:
            parent_current_node.left = Node(x)
            self.count_elements += 1


if __name__ == '__main__':

    elements = [int(i) for i in input().split()]
    binary_tree = BinaryTree()
    k = 0
    while elements[k] != 0:
        binary_tree.add_element(elements[k])
        k += 1

    print(binary_tree.count_elements)
