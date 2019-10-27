count_list_elements = int(input())

list_numbers = [int(i) for i in input().split()]

number = int(input())


def index_output(num_array, x):
    """Вывод номеров элементов, равному х"""
    for i in range(len(num_array)):
        if num_array[i] == x:
            print(i + 1, end=' ')  # так как индексация начинается с нуля


index_output(list_numbers, number)
