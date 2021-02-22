# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix():
    def __init__(self, A):
        self.m = [row[:] for row in A]

    def __str__(self):
        result = ""
        for row in self.m:
            for x in row:
                result += "{:<4}".format(x)
            result += "\n"
        return result

    def __add__(self, other):
        lst = [[0] * len(row) for row in self.m]
        for i in range(len(self.m)):
            for j in range(len(self.m[i])):
                lst[i][j] = self.m[i][j] + other[i][j]
        return Matrix(lst)

    def __getitem__(self, raw):
        return self.m[raw]

    def __len__(self):
        return len(self.m)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# просто печатаем "диагональную" неквадратную матрицу
# для проверки перегрузки
# методов __getitem__() и __len__()
b = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
for i in range(len(b)):
    for j in range(len(b[i])):
        if i == j:
            print(f"{b[i][j]:<4}", end="")
        else:
            print(f"{0:<4}", end="")
    print()

print()

# складываем две матрицы
a = m + n
print(a)
