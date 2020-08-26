'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём
оргтехники на склад и передачу в определенное подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
'''


# родительский класс оргтехники, в котором находятся все методы
class OrgTech:
    name: str
    model: str
    year: int
    price: float

    # конструктор
    def __init__(self, name, model, year, price):
        self.name = name
        self.model = model
        self.year = year
        self.price = price

    # присвоить складу из компании
    def move_to_stock_from_company(self, stock, company):
        if stock.check():
            stock.add(self)
            company.remove_tech(self)
        else:
            raise CapacityException(len(stock.list_of_tech), stock.max_count)

    # присвоить складу
    def move_to_stock(self, stock):
        if stock.check():
            stock.add(self)
        else:
            raise CapacityException(len(stock.list_of_tech), stock.max_count)

    # присвоить компании
    def move_to_company(self, company):
        if company.check():
            company.add(self)
        else:
            raise CapacityException(len(company.list_of_tech), company.max_count)

    # присвоить компании со склада
    def move_to_company_from_stock(self, company, stock):
        if company.check():
            company.add(self)
            stock.remove_tech(self)
        else:
            raise CapacityException(len(company.list_of_tech), company.max_count)

    # вывести базовую информацию
    def base_info(self):
        return f"{self.name} {self.model}, year: {self.year}. Cost: {self.price}"

    # красивый вывод
    def __str__(self):
        return f"{self.name} {self.model}, year: {self.year}. Cost: {self.price}"

    def __repr__(self):
        return self.__str__()


# класс принтера
class Printer(OrgTech):
    print_in_minute: int

    # переопределенный конструктор
    def __init__(self, name: str, model: str, year: int, price: float, print: float):
        super().__init__(name, model, year, price)
        self.print_in_minute = print


# класс сканера
class Scanner(OrgTech):
    scan_in_minute: int

    # переопределенный конструктор
    def __init__(self, name: str, model: str, year: int, price: float, scan: float):
        super().__init__(name, model, year, price)
        self.scan_in_minute = scan


# класс ксерокса
class Xerox(OrgTech):
    xerox_in_minute: int

    # переопределенный конструктор
    def __init__(self, name: str, model: str, year: int, price: float, xerox: float):
        super().__init__(name, model, year, price)
        self.xerox_in_minute = xerox


# класс компании
class Company:
    list_of_tech = []
    max_count: int

    # конструктор
    def __init__(self, max_count=0):
        self.max_count = max_count

    # добавить в компанию технику
    def add(self, obj):
        self.list_of_tech.append(obj)

    # проверка есть ли свободное место
    def check(self):
        return len(self.list_of_tech) < (self.max_count)

    # удаление техники
    def remove_tech(self, tech):
        self.list_of_tech.remove(tech)


# класс склада
class Stock:
    list_of_tech = []
    max_count: int

    # конструктор
    def __init__(self, max_count=0):
        self.max_count = max_count

    # добавить на склад
    def add(self, obj):
        self.list_of_tech.append(obj)

    # проверить, есть ли свободное место на складе
    def check(self):
        return len(self.list_of_tech) < (self.max_count)

    # убрать технику
    def remove_tech(self, tech):
        self.list_of_tech.remove(tech)


# исключение при отсутствии места на складе или компании
class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f"Not enough space. Current = {self.current}, needle = {self.needle}"


# класс валидации
class ValidTest:
    @staticmethod
    # проверить введенные данные для техники
    def check_tech(check: str):
        temp_mas = check.split(" ")
        if (not temp_mas[0].isdigit()) and (not temp_mas[1].isdigit()) and (2000 <= int(temp_mas[2]) <= 2020) and (
                0 <= float(temp_mas[3])) and (float(temp_mas[4]) >= 0):
            return True
        else:
            return False


while True:
    temp = input("Введите название, модель, год производства, цену и скорость работы ксерокса через пробел")
    try:
        if ValidTest.check_tech(temp):
            print(True)
            temp_str = temp.split(" ")
            xerox1 = Xerox(temp_str[0], temp_str[1], int(temp_str[2]), float(temp_str[3]), float(temp_str[4]))
        else:
            raise TypeError
        break
    except:
        print("Введено с ошибкой. Попробуйте проверить введенный год (от 2000 до 2020)")

while True:
    temp = input("Введите название, модель, год производства, цену и скорость работы сканера через пробел")
    try:
        if ValidTest.check_tech(temp):
            print(True)
            temp_str = temp.split(" ")
            scanner1 = Scanner(temp_str[0], temp_str[1], int(temp_str[2]), float(temp_str[3]), float(temp_str[4]))
        else:
            raise TypeError
        break
    except:
        print("Введено с ошибкой. Попробуйте проверить введенный год (от 2000 до 2020)")

while True:
    temp = input("Введите название, модель, год производства, цену и скорость работы принтера через пробел")
    try:
        if ValidTest.check_tech(temp):
            print(True)
            temp_str = temp.split(" ")
            printer1 = Printer(temp_str[0], temp_str[1], int(temp_str[2]), float(temp_str[3]), float(temp_str[4]))
        else:
            raise TypeError
        break
    except:
        print("Введено с ошибкой. Попробуйте проверить введенный год (от 2000 до 2020)")

print(xerox1.base_info())
print(scanner1.base_info())
print(printer1.base_info())

stock1 = Stock(2)
# кладем технику на склад
printer1.move_to_stock(stock1)
xerox1.move_to_stock(stock1)
# кладем сканер на склад, проверяя, есть ли там место
try:
    scanner1.move_to_stock(stock1)
except CapacityException as exception:
    print(exception)

company1 = Company(5)
# забираем ксерокс из склада и присваиваем компании
xerox1.move_to_company_from_stock(company1, stock1)
print(f"На складе осталось: {stock1.list_of_tech}")

'''
Результат

Введите название, модель, год производства, цену и скорость работы ксерокса через пробелveli 500xt 2019 5000 10
True
Введите название, модель, год производства, цену и скорость работы сканера через пробелveli2 400xt 2018 4560 15
True
Введите название, модель, год производства, цену и скорость работы принтера через пробелveli 
Введено с ошибкой. Попробуйте проверить введенный год (от 2000 до 2020)
Введите название, модель, год производства, цену и скорость работы принтера через пробелveli efo 2019 9380 20
True
veli 500xt, year: 2019. Cost: 5000.0
veli2 400xt, year: 2018. Cost: 4560.0
veli efo, year: 2019. Cost: 9380.0
Not enough space. Current = 2, needle = 2
На складе осталось: [veli efo, year: 2019. Cost: 9380.0]
'''
