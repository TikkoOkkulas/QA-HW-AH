#Написать функцию которая принимает целое число - number.
#Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'.
#Запрещено пользоваться функцией или оператором возведение в степень.

#Пример:
#is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
#is_power_of_two(125) # 'no' потому что это не степень двойки


def func(number):
    i = 1
    while i < number:
        i = i * 2
    if i == number:
        print("yes")
    else:
        print("no")

func(int(input('введите целое число - number: ')))