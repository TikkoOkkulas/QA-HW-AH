
#1
#Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
numbers = []
with open('data.txt', 'r') as x:
    i = x.read().split()
    for _ in i:
        if _.isdigit():
            numbers.append(_)
print(numbers)

#2
#Запросить у пользователя текст и записать его в файл data.txt
x = open('data2.txt', 'w')
x.write(input("введіть текcт: "))
x.close()

#3
#Запросить у пользователя число N и запросить N чисел у пользователя,
#потом записать их в файл numbers.txt через пробел
x = open('numbers.txt', 'w')
N = int(input("вкажіть число N: "))
A = []
for _ in range(N):
    A.append(int(input(f"введіть {_+1} число для списку: ")))
#A = [((input(f"введіть {_+1} число для списку: "))) for _ in range(N)]
print(*A, sep=' ', file=x)
x.close()

#4
#Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
import random
with open('random_numbers.txt', 'w') as x:
    a = [random.randint(1, 10) for _ in range(100)]
    for _ in a:
        x.write(str(f'{_}\n'))

#5
#Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
with open('data.txt', 'r') as x:
    A = x.read().split()
    i = 0
    for _ in A:
        if not _.isdigit():
            i += 1
    print("кількість слів в тексті = ", i)

#6
#Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
with open('numbers.txt', 'r') as x:
    A = x.read().split()
    print(A)
    S = 0
    for i in A:
        S = S+int(i)
    print('сума чисел = ', S)

#7
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' - 4
with open('data2.txt', 'r', encoding='utf-8') as f:
    A = f.read().split()
dict = {x:A.count(x) for x in A}
for i in sorted(dict, key=dict.get, reverse=True)[:5]:
    print(i, ' - ', dict[i], ' раз')