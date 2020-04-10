# Задача №745. Хеширование с удалением
# https://informatics.mccme.ru/mod/statements/view3.php?id=601&chapterid=745#1


class HashTable:
    def __init__(self):
        self.count_slices = 10
        self.size_each_slice = 100000
        self.table = []
        self.count_items_each_slice = [0] * self.count_slices

    def create_table(self):
        for i in range(self.count_slices):
            self.table.append([None] * self.size_each_slice)

    def add_element(self, item):
        expandable_slice_number = len(item) % self.count_slices

        if item not in set(self.table[expandable_slice_number]):
            self.table[expandable_slice_number][self.count_items_each_slice[expandable_slice_number]] = item
            self.count_items_each_slice[expandable_slice_number] += 1

    def search(self, item):
        index = len(item) % self.count_slices
        size_slice = self.count_items_each_slice[index]
        counter = 0
        while counter < size_slice:
            if self.table[index][counter] == item:
                return 'YES'

            counter += 1

        return 'NO'

    def delete(self, item):
        expandable_slice_number = len(item) % self.count_slices
        size_slice = self.count_items_each_slice[expandable_slice_number]
        counter = 0
        while counter < size_slice:
            if self.table[expandable_slice_number][counter] == item:
                self.table[expandable_slice_number].pop(counter)

                self.count_items_each_slice[expandable_slice_number] -= 1
                break

            counter += 1


if __name__ == '__main__':
    table = HashTable()
    command = input().split()
    table.create_table()
    while command[0] != '#':
        if command[0] == '+':
            table.add_element(command[1])

        if command[0] == '?':
            print(table.search(command[1]))

        if command[0] == '-':
            table.delete(command[1])

        command = input().split()
