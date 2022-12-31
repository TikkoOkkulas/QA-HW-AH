
# Написать итератор ReverseIterator который принимает список любых обьектов и итерируется по ним в обратном порядке.
# Нужно реализовать в виде класса.
# Важно: Нужно использовать аннотации.
# Пример:
# it = ReverseIterator([1, 2, 3, 4, 5])
#
# next(it)  # 5
# next(it)  # 4
# next(it)  # 3

class ReverseIterator:
    def __init__(self, data) -> any:
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        print(self.data[self.index])
        return self.data[self.index]


it = ReverseIterator([1, 2, 3, 4, 5])
next(it)  # 5
next(it)  # 4
next(it)  # 3