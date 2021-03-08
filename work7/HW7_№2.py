'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для
пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов
на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, parameters):
        self.parameters = parameters

    @property
    def consumption(self):
        return f'Сумма затраченной ткани равна: {self.parameters / 6.5 + 0.5 + 2 * self.parameters + 0.3 }'

    @abstractmethod
    def abstract(self):
         pass



class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.parameters / 6.5 + 0.5 } ткани'

    def abstract(self):
        pass


class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.parameters + 0.3 } ткани'

    def abstract(self):
        pass


coat = Coat(322)
costume = Costume(34)
print(costume.consumption())



