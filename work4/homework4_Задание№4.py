'''4. Представлен список чисел. Определить элементы списка,
не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их
следования в исходном списке. Для выполнения задания обязательно
использовать генератор.'''



my_list = [3, 2, 5, 2, 10, 2, 11, 10, 15, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_list)
print(my_new_list)

