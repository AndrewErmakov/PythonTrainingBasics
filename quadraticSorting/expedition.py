# Задача №1426. Экспедиция
# https://www.informatics.mccme.ru/mod/statements/view3.php?id=271&chapterid=1426#1


def shell_sorting(nums: list, len_nums: int) -> list:
    """Возвращает отсортированный список значений"""
    distance = len_nums // 2

    while distance > 0:
        for i in range(len_nums - distance):
            j = i
            while j >= 0 and nums[j] > nums[j + distance]:
                nums[j], nums[j + distance] = nums[j + distance], nums[j]
                j -= 1

        distance //= 2

    return nums


def creating_list_rafts_payload(n: int, m: int) -> list:
    """Создает список значений грузоподъемности плотов"""
    rafts_payload = []
    for i in range(n):
        rafts_values_payload = [int(k) for k in input().split()]
        for j in range(m):
            rafts_payload.append(rafts_values_payload[j])

    return rafts_payload


number_rafts_vertically, number_rafts_horizontally = map(int, input().split())
sorted_list_rafts_payload = shell_sorting(
    creating_list_rafts_payload(number_rafts_vertically, number_rafts_horizontally),
    number_rafts_vertically * number_rafts_horizontally)

number_tourists = int(input())
sorted_list_mass_tourists = shell_sorting([int(i) for i in input().split()], number_tourists)
count_tourists_journey = 0
index_busy_rafts_list = []

for i in range(number_tourists):
    raft_occupied_index = None
    for j in range(number_rafts_vertically * number_rafts_horizontally):
        if sorted_list_mass_tourists[i] <= sorted_list_rafts_payload[j] and j not in index_busy_rafts_list:
            raft_occupied_index = j
            break

    if raft_occupied_index is not None:
        count_tourists_journey += 1
        index_busy_rafts_list.append(raft_occupied_index)

print(count_tourists_journey)



