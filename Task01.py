'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
@classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Date:
    date_format: str
    __days = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    def __init__(self, date: str):
        self.date_format = date

    def __str__(self):
        return Date.date_format

    def get_format(self):
        return self.date_format

    @classmethod
    def turn_date(cls, date):
        temp_mas = date.split('-')
        day = int(temp_mas[0])
        month = int(temp_mas[1])
        year = int(temp_mas[2])

        return f"Сейчас: {year} год, {month} месяц, {day} день."

    @staticmethod
    def check_date(date: str):
        temp_mas = date.split('-')
        day = int(temp_mas[0])
        month = int(temp_mas[1])
        year = int(temp_mas[2])

        if (1 <= day <= Date.__days[month]) and 1 <= month <= 12 and 0 <= year <= 2020:
            return True
        else:
            return False


if Date.check_date("22-04-2020"):
    new_date = Date("22-04-2020")
    print(new_date.turn_date(new_date.date_format))
    print(new_date.date_format)
else:
    print("Неверная дата")

'''
Результат

Сейчас: 2020 год, 4 месяц, 22 день.
22-04-2020
'''
