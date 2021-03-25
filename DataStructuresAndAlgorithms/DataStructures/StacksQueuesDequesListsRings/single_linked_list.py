class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def add_to_end(self, value):
        """Добавление элемента списка с определенным значением в конец"""
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = Node(value)

        self.length += 1

    def add_to_beginning(self, value):
        """Добавление элемента списка с определенным значением в начало"""
        if self.head is None:
            self.head = Node(value)

        current_node = self.head
        self.head = Node(value=value, next=current_node)

    def add_after_certain_node(self, certain_value, insert_value):
        if self.is_list_empty():
            return 'Список пуст'
        current_node = self.head
        while current_node is not None:
            if current_node.value == certain_value:
                if current_node.next is None:
                    current_node.next = Node(insert_value)
                else:
                    next_element = current_node.next
                    current_node.next = Node(value=insert_value, next=next_element)
                self.length += 1
                return True
            else:
                current_node = current_node.next
        return False

    def remove(self, pointer):
        """Удаление узла из списка с определенным значением"""
        if self.is_list_empty():
            return 'Список пустой, нечего удалять'

        previous_node, current_node = None, self.head

        while current_node is not None:
            if current_node.value == pointer:
                if previous_node is None:
                    # если удаляемый элемент самый первый
                    self.head = current_node.next
                elif current_node.next is None:
                    # если удаляемый элемент самый последний
                    previous_node.next = None
                else:
                    previous_node.next = current_node.next

                self.length -= 1
                return True
            else:
                previous_node, current_node = current_node, current_node.next

        return False

    def print_elements_list(self):
        """Вывод списка по порядку"""
        if self.head is None:
            print('Список пустой')
        else:
            current_node = self.head
            print(current_node.value, end=' ')
            while current_node.next is not None:
                current_node = current_node.next
                print(current_node.value, end=' ')

    def clean_list(self):
        """Очистка списка"""
        self.head = None
        self.length = 0

    def get_length(self):
        """Получение длины списка"""
        return self.length

    def is_list_empty(self):
        """Проверка пуст ли список"""
        return self.length == 0


if __name__ == '__main__':
    lst = LinkedList()
    for _ in range(5):
        lst.add_to_end(int(input('Введите число: ')))
    lst.print_elements_list()
    lst.remove(int(input('Какое число удалить: ')))
    print('Список после удаления')
    lst.print_elements_list()
    lst.add_to_beginning(int(input('Какой элемент вставить вначале: ')))
    lst.add_after_certain_node(3, 9)
    # lst.clean_list()
    # print('Список после очистки')
    lst.print_elements_list()
    # print(lst.is_list_empty())
