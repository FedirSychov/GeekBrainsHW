'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс
«Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''


class CompNum:
    real_part: float
    imagine_part: float

    def __init__(self, Re, Im):
        self.real_part = Re
        self.imagine_part = Im

    def __str__(self):
        return f"({self.real_part}, {self.imagine_part})"

    def __add__(self, other):
        return CompNum(self.real_part + other.real_part, self.imagine_part + other.imagine_part)

    def __sub__(self, other):
        return CompNum(self.real_part - other.real_part, self.imagine_part - other.imagine_part)

    def __mul__(self, other):
        return CompNum((self.real_part * other.real_part - self.imagine_part * other.imagine_part),
                       (self.real_part * other.imagine_part + self.imagine_part * other.real_part))


first_num = CompNum(5, 6)
second_num = CompNum(1, 2)
# сложение и вычитание комплексных чисел
third_num = first_num - second_num
print(f"Из числа {first_num} вычесть число {second_num}. Получится {third_num}")
third_num = first_num + second_num
print(f"К числу {first_num} прибавить число {second_num}. Получится {third_num}")
# Произведение
forth_num = first_num * second_num
print(f"Произведение первого и второго числа равно {forth_num}")

'''
Результат

Из числа (5, 6) вычесть число (1, 2). Получится (4, 4)
К числу (5, 6) прибавить число (1, 2). Получится (6, 8)
Произведение первого и второго числа равно (-7, 16)
'''
