# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через
# list и через dict.

year_list = [ 'зимы', 'весна', 'лето', 'осень']
year_dict = {1 : 'зимы', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите месяц под номеру "))
if month == 1 or month == 12 or month == 2:
    print(f"Это периуд {year_dict.get(1)}, в это время года холодно, так что оденься теплее!!!")
    print(f"Это периуд {(year_list[0])}, в это время года холодно, так что оденься теплее!!!")
elif month == 3 or month == 4 or month == 5:
    print(year_dict.get(2))
    print(year_list[1])
elif month == 6 or month == 7 or month == 8:
    print(year_dict.get(3))
    print(year_list[2])
elif month == 9 or month == 10 or month == 11:
    print(year_dict.get(4))
    print(year_list[3])
else:
    print("Такого месяца не существует")