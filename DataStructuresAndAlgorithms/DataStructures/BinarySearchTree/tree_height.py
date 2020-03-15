# Задача №757. Высота дерева
# https://informatics.mccme.ru/mod/statements/view.php?id=599#1


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left: Node = None
        self.right: Node = None


class BinaryTree:
    def __init__(self):
        self.root: Node = None
        self.height_tree: int = 0

    def add_element(self, x: int):
        if self.root is None:
            self.root = Node(x)
            self.height_tree += 1
            return

        current_node: Node = self.root
        parent_current_node: Node = None

        current_height = 1

        while current_node is not None:
            parent_current_node = current_node

            if x > current_node.value:
                current_node = current_node.right
                current_height += 1

            elif x < current_node.value:
                current_node = current_node.left
                current_height += 1

            else:
                break

        if x > parent_current_node.value:
            parent_current_node.right = Node(x)
        else:
            parent_current_node.left = Node(x)

        if current_height > self.height_tree:
            self.height_tree = current_height


if __name__ == '__main__':

    elements = [int(i) for i in input().split()]
    binary_tree = BinaryTree()
    k = 0
    while elements[k] != 0:
        binary_tree.add_element(elements[k])
        k += 1

    print(binary_tree.height_tree)
