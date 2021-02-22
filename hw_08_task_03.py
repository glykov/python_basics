# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class InputError(Exception):
    def __init__(self, wired_input):
        self.text = f"{wired_input} is not a number!"


def make_number(some_input):
    sign = 1
    if some_input[0] == '-':
        sign = -1
        some_input = some_input[1:]
    if '.' in some_input:
        n, r = some_input.split('.')
        if n.isdigit() and r.isdigit():
            return float(some_input) * sign
    elif some_input.isdigit():
        return int(some_input) * sign
    else:
        raise InputError(some_input)


data_list = []
print("Enter number followed by <Enter>")
print("To stop - print 'stop'")
while(True):
    a = input()
    if a.lower() == "stop":
        break
    try:
        el = make_number(a)
    except InputError as e:
        print(e.text)
        print("try again!")
    else:
        data_list.append(el)

print(data_list)
