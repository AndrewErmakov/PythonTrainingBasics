class HashTable:
    def __init__(self):
        self.size = 10
        self.table = []

    def create_table(self):
        for i in range(self.size):
            self.table.append([])

    def add_element(self, item):
        index = len(item) % self.size
        self.table[index].append(item)

    def search(self, item):
        index = len(item) % self.size
        size_slice = len(self.table[index])
        counter = 0
        while counter < size_slice:
            if self.table[index][counter] == item:
                return 'YES'

            counter += 1

        return 'NO'


if __name__ == '__main__':
    table = HashTable()
    command = input().split()
    table.create_table()
    while command[0] != '#':
        if command[0] == '+':
            table.add_element(command[1])

        if command[0] == '?':
            print(table.search(command[1]))

        command = input().split()
