# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __repr__(self):
        return f'({self.real} + {self.img}i)' if self.img > 0 else f'({self.real} - {abs(self.img)}i)'

    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)

    def __mul__(self, other):
        r = self.real * other.real - self.img * other.img
        i = self.img * other.real + other.img * self.real
        return Complex(r, i)

    def __truediv__(self, other):
        d = other.real ** 2 + other.img ** 2
        r = (self.real * other.real + self.img * other.img) / d
        i = (self.img * other.real - self.real * other.img) / d
        return Complex(r, i)


a = Complex(1, 3)
b = Complex(4, -5)
print("a:", a)
print("b:", b)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
