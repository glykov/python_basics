# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    '''возвращает сумму наибольших двух аргументов'''
    return a + b + c - min(a, min(b, c))


print(my_func(100, 25, 50))
