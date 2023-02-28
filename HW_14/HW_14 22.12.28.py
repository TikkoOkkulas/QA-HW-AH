# Создайте супер класс Shape и его наследников Triangle, Rectangle.
# Класс Shape содержит абстрактный метод draw
# Класс Triangle в инициализаторе принимает параметр width: int - ширина треугольника и реализует метод draw
# (Выводит в консоль треугольник с шириной width)
# Класс Rectangle в инициализаторе принимает параметр width: int и height: int - ширина, высота прямоугольника
# и реализует метод draw (Выводит в консоль прямоугольник с шириной width и высотой height)
# Создайте список с этими фигурами и в цикле вызовите метод draw у этих обьектов

# P.S. Треугольник может быть любой (Равносторонний, Равнобедренный, Разносторонним)
# главное чтобы состоял и был заполнен символом '*'.
# Прямоугольник тоже должен состоять и быть заполнен символом '*'.
# Важно: Используйте аннотации!

class Shape():
    def draw(self):
        raise NotImplemented

class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width
    def draw(self):
        for i in range(self.width, 0, -1):
            print('*' * i)

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    def draw(self):
        print(('*' * self.width + '\n') * self.height)

def run(obj: Shape):
    if not isinstance(obj, Shape):
        raise ValueError
    obj.draw()

run(Triangle(width = int(input('Вкажіть width = '))))

run(Rectangle(width = int(input('Вкажіть width = ')), height = int(input('Вкажіть height = '))))

