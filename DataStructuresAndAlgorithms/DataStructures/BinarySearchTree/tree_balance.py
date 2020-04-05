# Задача №764. Сбалансированность
# https://informatics.mccme.ru/mod/statements/view3.php?id=599&chapterid=764#1


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Node = None
        self.right: Node = None
        self.node_height = 0
        self.is_balanced: bool = True


class BinaryTree:
    def __init__(self):
        self.root: Node = None

    def add_element(self, x: int):
        if self.root is None:
            self.root: Node = Node(x)
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

        elif x < parent_current_node.value:
            parent_current_node.left = Node(x)

    def visit(self, node: Node):
        height = 1
        if node.left is not None:
            self.visit(node.left)
            height = node.left.height + 1

        if node.right is not None:
            self.visit(node.right)

            height = max(height, node.right.height + 1)

        node.height = height

    def check_is_balanced(self, node: Node):
        left_height = 0
        right_height = 0

        left_balanced = True
        right_balanced = True

        if node.left is not None:
            left_height = node.left.height
            self.check_is_balanced(node.left)
            left_balanced = node.left.is_balanced

        if node.right is not None:
            right_height = node.right.height
            self.check_is_balanced(node.right)
            right_balanced = node.right.is_balanced

        node.is_balanced = right_balanced and left_balanced and abs(right_height - left_height) <= 1
        return node.is_balanced

    def summary(self):
        self.visit(self.root)
        result = self.check_is_balanced(self.root)
        if result:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    elements = [int(i) for i in input().split()]
    binary_tree = BinaryTree()
    k = 0
    while elements[k] != 0:
        binary_tree.add_element(elements[k])
        k += 1
    print(binary_tree.summary())
