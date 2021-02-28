'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке
'''

with open('test.txt', 'r') as my_f:
    lines = my_f.readlines()
    print(f"Всего строк: {len(lines)}")
    for line in lines:
        print(f"'{line[:]}' СЛОВ В СТРОКЕ -  {len(line)}")