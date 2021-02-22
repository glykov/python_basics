# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, title):
        self.title = title.title()

    @abstractmethod
    def calculate_fabric(self):
        pass


class Coat(Clothing):
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 15:
            size = 15
        elif size > 50:
            size = 50
        else:
            self.__size = size

    @size.getter
    def size(self):
        return self.__size

    def calculate_fabric(self):
        return self.__size / 6.5 + 0.5


class Suit(Clothing):
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1.5:
            self.__height = 1.5
        elif height > 2.2:
            self.__height = 2.2
        else:
            self.__height = height

    @height.getter
    def height(self):
        return self.__height

    def calculate_fabric(self):
        return 2 * self.__height + 0.3


c = Coat('supercoat')
c.size = 38
total_fabric = c.calculate_fabric()
# проверяем геттер
print(f"to make the {c.title} of size {c.size}")
print("we need {:.2f} m2 of fabric\n".format(c.calculate_fabric()))
# проверяем сеттер
c.size = 40
total_fabric += c.calculate_fabric()
print(f"to make the {c.title} of size {c.size}")
print("we need {:.2f} m2 of fabric\n".format(c.calculate_fabric()))

s = Suit('megasuit')
s.height = 1.8
total_fabric += s.calculate_fabric()
print(f"to make the {s.title} for height {s.height}")
print("we need {:.2f} m2 of fabric\n".format(s.calculate_fabric()))

print(f"totally we need {total_fabric:.2f} m2 of fabric")
