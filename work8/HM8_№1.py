'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например,
месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных.
'''

class Data:
    def __init__(self, day_m_y):
        self.day_m_y = day_m_y

    @classmethod
    def chislo(cls, date: "Data"):
        return list(map(int, date.day_m_y.split("-")))

    @staticmethod
    def validation(date: "Data"):
        parsed_data = date.day_m_y.split("-")
        if len(parsed_data[2]) not in {2, 4}:
            raise ValueError("Невалидный год")
        if not 1 <= int(parsed_data[1]) <= 12:
            raise ValueError("Невалидный Месяц")
        if not 1 <= int(parsed_data[0]) <= 31:
            raise (ValueError("евалидное чилсо"))
        print("Вадижация успешно пройдена")


date = Data("10-01-2020")
date.validation(date)
print(Data.chislo(date))