number_countries = int(input())

dict_countries = dict()

for i in range(number_countries):
    country_cities = input().split()
    for city in country_cities[1:]:
        dict_countries[city] = country_cities[0]

numb_find_cities = int(input())

for k in range(numb_find_cities):
    find_city = input()
    if find_city in dict_countries:
        print(dict_countries[find_city])
