'''
3. Создайте собственный класс-исключение, который должен проверять содержимое
списка на наличие только чисел. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
'''


class AllNumsException(Exception):
    def __str__(self):
        return (f"В списке присутствуют нечисловые значения!")


class Test:
    list: list

    def __init__(self, lists):
        self.list = lists

    def check(self):
        check = True
        for el in self.list:
            if not str(el).isdigit():
                check = False
                raise AllNumsException
        return check


test2 = []
print("Вводите числа, чтобы заносить их в список. Для окончания ввода напишите stop")
while True:
    temp = input()
    if temp == "stop":
        break
    try:
        if temp.isdigit():
            test2.append(temp)
        else:
            raise AllNumsException
    except AllNumsException as exception:
        print(exception)

print(test2)
