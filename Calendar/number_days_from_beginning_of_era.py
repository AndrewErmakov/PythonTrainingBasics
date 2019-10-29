date = input()

current_day = int(date[0:2])
current_month = int(date[2:4])
current_year = int(date[4:])

num_days = 0

for year in range(1, current_year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # проверка на високосность года
        num_days += 366

    else:
        num_days += 365

list_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if current_year % 4 == 0 and current_year % 100 != 0 or current_year % 400 == 0:  # проверка на високосность года
    list_days_in_month[1] = 29
    
for month in range(current_month - 1):  # перевод сегодняшней даты в число дней от начала года
    num_days += list_days_in_month[month]

num_days += current_day

print(num_days)

