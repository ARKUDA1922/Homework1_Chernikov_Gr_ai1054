'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе
пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
'''

class MyZeroDivisinError(Exception):
    def __init__(self, txt="Дуление на ноль!"):
        self.txt = txt


def my_func(a, b):
    if b==0:
        raise MyZeroDivisinError("You give negative!!!")
    return a / b


try:
    print(my_func(1, 0))
except MyZeroDivisinError as err:
    print(err)