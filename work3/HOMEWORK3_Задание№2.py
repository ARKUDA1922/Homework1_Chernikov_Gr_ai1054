'''
2. Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email,
телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

'''
name = input('Введите ваше имя : ')
surname = input('Введите вашу фамилию : ')
year = input('Введите ваш взораст : ')
city = input('Введите ваш город : ')
email = input('Введите ваш EMAIL  : ')
phone = input('Введите ваш ваш номер телефона  :+7 ')
'''
def my_func(name, surname, year, city, email, phone):
    return " ".join([name, surname, year, city, email, phone])
print((my_func(name = 'Михаил',surname = 'Черников', year = '21', city = 'Мытищи', email = 'tumtum2011@yandex.ru', phone = '+79263236123')))
