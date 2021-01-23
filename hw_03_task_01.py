# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(first, second):
    '''Функция возвращает результат деления first на second'''
    return first / second


while True:
    s = input("Введите два числа через пробел (для выхода нажмите q): ")
    if s.lower() == 'q':
        break
    try:
        a, b = s.split()
        a = int(a)
        b = int(b)
    except ValueError as ve:
        print("Вы не ввели два числа")
        print(ve)
    else:
        if b == 0:
            print("Второе число должно быть отлично от нуля")
        else:
            print(f"Результат деления: {division(a, b)}")
