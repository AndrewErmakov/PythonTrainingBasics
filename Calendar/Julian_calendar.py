list_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

number_days_in_year = int(input())
num_days = num_month = 0
for days in list_days_in_month:
    if number_days_in_year > days:
        number_days_in_year -= days

    else:
        num_days = number_days_in_year % (days + 1)
        num_month += 1
        break

    num_month += 1
print(num_days, num_month)

