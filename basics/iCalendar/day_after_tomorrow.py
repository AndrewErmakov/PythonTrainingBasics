list_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

current_day, current_month, current_year = map(int, input().split())

number_days = current_day

if (current_year % 4 == 0 and current_year % 100 != 0) or current_year % 400 == 0:  # проверка на високосность года
    list_days_in_month[1] = 29

for i in range(current_month - 1):  # перевод сегодняшней даты в число дней от начала года
    number_days += list_days_in_month[i]

number_days += 2  # номер послезавтрашнего дня

num_month = num_days = 0
num_year = current_year
if number_days > sum(list_days_in_month):
    num_days = number_days % sum(list_days_in_month)
    num_month = 1
    num_year += 1

else:
    for days in list_days_in_month:
        if number_days > days:
            number_days -= days
        #
        else:
            num_days = number_days % (days + 1)
            num_month += 1
            break
        #
        num_month += 1

print(num_days, num_month, num_year)

