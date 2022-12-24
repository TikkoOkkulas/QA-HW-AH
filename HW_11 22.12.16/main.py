
# Написать декоратор call_times, который будет принимать в качестве параметра file_name,
# считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'


A = {}
def call_times(file_name):
    def inner(func):
        def wrapper():
            wrapper.count += 1
            A[func.__name__] = wrapper.count
            with open(file_name, 'w', encoding='utf-8') as f:
                for func_name, count in A.items():
                    f.write(f'{func_name} была вызвана {count} раза.\n')
            return func()
        wrapper.count = 0
        return wrapper
    return inner
@call_times('foo.txt')
def foo():
  pass
@call_times('foo.txt')
def boo():
  pass
@call_times('calls.txt')
def doo():
  pass

foo()
boo()
foo()
foo()
boo()
dict.clear(A)
doo()

# Пример:
# @call_times('foo.txt')
# def foo():
#   pass
#
# @call_times('foo.txt')
# def boo():
#   pass
#
# @call_times('calls.txt')
# def doo():
#   pass
#
# foo()
# boo()
# foo()
# foo()
# boo()
# doo()

#Файл foo.txt:
#foo была вызвана 3 раза
#boo была вызвана 2 раза
#Файл calls.txt:
#doo была вызвана 1 раза
