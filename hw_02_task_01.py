# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

number_elements = int(input("Сколько элементов данных Вы хототе ввести?: "))
data = []

for i in range(number_elements):
    element = input()
    # проверка на тип bool
    if element == 'True' or element == 'False':
        data.append(bool(element))
    # проверка на тип float производится если в строке есть одна точка
    elif '.' in element and element.count('.') == 1:
        is_float = True
        # проверяем каждый знак введенной строки, если он не точка и не цифра,
        # значит, приветси к float не удасться
        for ch in element:
            if ch != '.' and not ch.isdigit():
                is_float = False
        if is_float:
            data.append(float(element))
        else:
            data.append(element)
    # проверка на тип int
    elif element.isdigit():
        data.append(int(element))
    # если все предыдущие проверки не сработали - считаем введенное значение строкой
    else:
        data.append(element)

# выводим список с нумерацией элементов
for i, item in enumerate(data, 1):
    print(f'{i}-й элемент имеет тип {type(item)}')
