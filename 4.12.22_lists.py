
#1:
print("Запросить у пользователя 5 чисел и записать их в список")
list = []
for _ in range(5):
    list.append(int(input(f'введіть {_+1} число для списку: ')))
print(list)


#2:
print("Дан список A = [1, 2, 3, 4, 5]. Удалить последнее число из списка")
A = [1, 2, 3, 4, 5]
A.pop()
print(A)
A.clear() #вписав, щоб не заважало іншим задачам

#3:
print("Запросить у пользователя 10 чисел и записать их в список A\
     Запросить у пользователя число N\
     Вывести пользователю сколько в списке A повторяется число N")
A = []
for _ in range(10):
    A.append(int(input(f"введіть {_+1} число для списку: ")))
N = int(input("вкажіть число N: "))
print(f" число {N} повторюється {A.count(N)} разів")
A.clear()

#4:
print("Запросить у пользователя число N \
     Запросить у пользователя N чисел и записать их в список A \
     Вывести список в обратной последовательности")
N = int(input("вкажіть число N: "))
A = []
for _ in range(N):
    A.append(int(input(f"введіть {_+1} число для списку: ")))
print(A[::-1])
A.clear()

#5:
print("Запросить у пользователя 5 чисел и записать их в список A \
     Записать все числа из списка A которые больше 5 в список C")
A = []
for _ in range(5):
    A.append(int(input(f'введіть {_+1} число для списку: ')))
C = []
for i in A:
    if i > 5:
        C.append(i)
print(C)
A.clear()

#6:
print("Запросить у пользователя число N \
Запросить у пользователя N целых чисел и записать их в список A \
Найти в нем минимальное и максимальное число с помощью цикла \
(запрещено использовать функцию min и max). Вывести эти числа.")
N = int(input("вкажіть число N: "))
A = []
for _ in range(N):
    A.append(int(input(f"введіть {_+1} число для списку: ")))
max = A[0]
min = A[1]
for i in A:
    if i > max:
        max = i
    else:
        min = i
print("максимальне значення = ", max)
print("мінімальне значення = ", min)
A.clear()

#7:
print("Пользователь вводит текст нужно вывести количество чисел в этом тексте \
Пример: 'Lorem 222 ipsum, 123 dolor 1 sit amet' Количество чисел: 3")
string = (input("введіть текст: "))
A = string.split(" ")
x = 0
for _ in A:
    if _.isdigit():
        x += 1
print("кількість чисел в тексті = ", x)
