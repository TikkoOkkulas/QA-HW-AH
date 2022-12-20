
'''Необходимо создать класс Human с атрибутами:
name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__

Так-же нужно написать методы:

get_info(self) - который возвращает словарь в котором находится информация о человеке
call(self, phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info'''

class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address
    def get_info(self):
        for key, value in Human():
            print(key, " :: ", value)
    def call(self, phone_number):
        print(f'{self.phone} вызывает абонента {phone_number}')

tom = Human('Tom', 'Tomson', 11, '+1111111111', 'NY')
rob = Human('Rob', 'Robson', 22, '+222222222', 'Paris')
john = Human('Tom', 'Tomson', 33, '+333333333', 'Ife')
tom.get_info()
tom.call(rob.phone)
rob.get_info()
rob.call(tom.phone)
john.get_info()
john.call(tom.phone)

#методи прописав після всіх хуманов, бо том не бачив телефон роба, який описувався нижче методів