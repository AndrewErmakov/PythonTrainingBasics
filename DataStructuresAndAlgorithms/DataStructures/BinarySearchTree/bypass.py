# Задача №760. Обход
# https://informatics.mccme.ru/mod/statements/view3.php?id=599&chapterid=760#1


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

    def delete_min_element(self):
        """
        Delete this minimal element
        """
        if self.root is None:
            return
        # search minimum in BST
        min_item: Node = self.root
        parent_node = None
        while min_item.left is not None:
            parent_node = min_item
            min_item = min_item.left
        result = min_item.value

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
    count_elements = binary_tree.count_elements
    for _ in range(count_elements):
        print(binary_tree.delete_min_element())
