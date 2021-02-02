# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

class Cell():
    def __init__(self, number=1):
        # решаем проблему с отрицательным количеством ячеек :-)
        self.__number = abs(number)

    @property
    def number(self):
        return self.__number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        try:
            return Cell(round(self.number / other.number))
        except ZeroDivisionError as zd:
            print(zd)
            return Cell()

    def make_order(self, cells_in_row):
        rows = self.__number // cells_in_row
        rem = self.__number % cells_in_row
        res = ('@ ' * cells_in_row + '\n') * rows + '@ ' * rem
        return res


a = Cell(20)
b = Cell(5)
c = a + b
print(c.number)
print(c.make_order(7))
print()

d = a - b
print(d.number)
print(d.make_order(8))
print()

e = a * b
print(e.number)
print(e.make_order(10))
print()

f = a / b
print(f.number)
print(f.make_order(7))
print()

g = Cell(10) / Cell(0)
print(g.make_order(10))
