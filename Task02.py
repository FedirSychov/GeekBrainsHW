'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class ZeroDivisionException(Exception):
    first: float
    second: float

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return f"Допущена ошибка деления на ноль! Делимое = {self.first}, делитель = {self.second}"


a = 5
b = 0
try:
    if b == 0:
        raise ZeroDivisionException(a, b)
    else:
        print(a / b)
except ZeroDivisionException as exception:
    print(exception)

'''
Результат

Допущена ошибка деления на ноль! Делимое = 5, делитель = 0
'''
