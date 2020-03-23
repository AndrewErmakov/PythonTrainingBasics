# Задача №762. Вывод развилок
# https://informatics.mccme.ru/mod/statements/view3.php?id=599&chapterid=762#1
from copy import deepcopy


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
        """
        function to add a node to the current binary search tree
        :param x:  value added
        """
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

    def is_node_fork(self, x: Node, original_tree: Node):
        """
        check for children in the node, therefore the node is a fork
        :param x: checked node
        :param original_tree: original binary tree
        :return: 1. value of node if node is a fork
                 2. None if the node has less than two children
        """
        while True:
            if x.value == original_tree.value:
                if original_tree.left is not None and original_tree.right is not None:
                    return x.value
                else:
                    return None
            elif x.value > original_tree.value:
                original_tree = original_tree.right

            else:
                original_tree = original_tree.left

    def is_node_leaf(self, x: Node, original_tree: Node):
        """
        checking the node for the absence of both children by searching for the node in the original tree
        :param x: checked node
        :param original_tree: original binary tree
        :return: 1. value of node if not having children
                 2. None if there is at least one child
        """
        while True:
            if x.value == original_tree.value:
                if original_tree.left == original_tree.right is None:
                    return x.value
                else:
                    return None
            elif x.value > original_tree.value:
                original_tree = original_tree.right

            else:
                original_tree = original_tree.left

    def delete_min_element(self, tree: Node):
        """
        Delete this minimal element
        """
        if self.root is None:
            return

        # search minimum in BST
        min_item: Node = self.root
        parent_node: Node = None

        while min_item.left is not None:
            parent_node = min_item
            min_item = min_item.left

        result = self.is_node_fork(min_item, tree)

        # if only one item is left in BTS
        if self.count_elements == 1:
            return result

        # if the deleted item of BTS does not have a right child
        elif min_item.right is None:
            parent_node.left = None

        # if the deleted item of BTS have a right child
        else:
            child = min_item.right
            parent_node = min_item
            parent_node.left = child.left
            parent_node.right = child.right
            parent_node.value = child.value

        self.count_elements -= 1

        return result


if __name__ == '__main__':

    elements = [int(i) for i in input().split()]
    binary_tree = BinaryTree()
    k = 0
    while elements[k] != 0:
        binary_tree.add_element(elements[k])
        k += 1

    # making a copy of the original tree (full)
    total_BST = deepcopy(binary_tree.root)

    count_elements = binary_tree.count_elements
    for _ in range(count_elements):
        leaf = binary_tree.delete_min_element(total_BST)
        if leaf is not None:
            print(leaf)
