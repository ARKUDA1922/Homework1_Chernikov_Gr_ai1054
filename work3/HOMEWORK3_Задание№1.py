''' 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
 выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
 обработку ситуации деления на ноль.
 '''

def div(*meaning):

   try:
       meaning1 = int(input("Введите ваше 1 число: "))
       meaning2 = int(input("Введите ваше 2 число: "))
       res = meaning1 / meaning2
   except ValueError:
       return 'Value error'
   except ZeroDivisionError:
       return "Не то значение! Вы не можете использовать ноль в качестве делителя!"

   return res

   '''
    if meaning2 != 0:
        :return meaning1 / meaning2
    else:
        print(Не то значение! Вы не можете использовать ноль в качестве делителя!)
    '''

print(f'Результат:  {div()}')