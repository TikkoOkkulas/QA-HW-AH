#1
# Напишите функцию change(lst), которая принимает список и меняет местами его первый
# и последний элемент. В исходном списке минимум 2 элемента.
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
A = [1, 2, 3, 4]
print('new list =', change(A))

#2
# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
def to_dict(lst):
    new_dict = {i: i for i in lst}
    return new_dict
A = [1, 2, 3, 4]
print('new dict =', to_dict(A))

#3
# Напишите функцию sum_range(start, end),
# которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
def sum_range(start, end):
    if start > end:
        start, end = end, start
    summ = 0
    for i in range(start, end + 1):
        summ += i
    return summ
A = (input('введите 2 или больше чисел через пробел: ').split())
for i in range(len(A)):
    A[i] = int(A[i])
print('sum =', sum_range(A[0], A[-1]))
# треба мабуть було перепитати щодо завдання, бо не зовсім зрозумів нащо міняти місцями числа
# ("від перестановки доданків... і далі по тексту"))

#4
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
def read_last(lines, file):
    if not lines > 0:
        print('не задано положительное целое число')
    else:
        with open(file, 'r') as file:
            data = file.readlines()[-lines:]
        for i in data:
            print(i.strip())
read_last(int(input('сколько последних строк вивести: ')), 'data.txt')