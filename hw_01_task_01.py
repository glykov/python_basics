# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
# маленький калькулятор
a = int(input('Введите целое число: '))
b = int(input('Введите целое число: '))
operation = input('Введите знак операции (+, -, /, *, mod, pow, div): ')

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == 'pow':
    print(a ** b)
# остались операции деления -- проверить b != 0
elif b != 0:
    if operation == '/':
        print(a / b)
    elif operation == 'mod':
        print(a % b)
    elif operation == 'div':
        print(a // b)
elif b == 0:
    print('Деление на 0!')
else:
    print('Операция не определена')
