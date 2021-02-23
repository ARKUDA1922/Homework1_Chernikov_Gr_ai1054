'''1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать
формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.'''
from sys import argv


def sal(time, salary, bonus):
    try:
        time = int(time)
        salary = int(salary)
        bonus = int(bonus)
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
        print(f"Зарплата- {sal(*map( argv[1:]))}")
    except ValueError:
        print('Not a number')