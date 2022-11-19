# Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Найдите наибольшее число из них и запишите в переменную max.

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# даний варіант рішення, якщо опиратись на пройдений матеріал
if (a > b) and (a > c):
    max = a
    print(max)
elif (b > a) and (b > c):
    max = b
    print(max)
elif (c > a) and (c > b):
    max = c
    print(max)
else:
    print("the numbers are equal, try next")


"""
також згадав більш швидкий варіант
if a != b or a != c or b != c:
    max = max(a, b, c)
    print(max)
else:
    print("the numbers are equal, try next")
"""
