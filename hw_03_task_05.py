# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum(args):
    '''Возвращает сумму чисел, полученных в аргументе'''
    result = 0
    for arg in args:
        result += arg
    return result
# не стал использовать *args, т.к. передаю в функцию список,
# который упаковывается в кортеж из-за *args.
# насколько я понял, *args хорошо использовать, если переменное количество аргументов
# передается непосредственно программистом в разных местах программы,
# если же мы получаем ввод от пользователя неизвестной длинны, легче использовать
# параметр в виде списка.
# Не могли бы Вы остановиться на этом вопросе подробнее при разборе домашнего задания?


done = False
result = 0
while not done:
    nums = []
    s = input(
        "Введите строку чисел, разделенных пробелами (для выхода введите нецифровой символ): ")
    try:
        s = s.split()
    except:
        # если введен один символ и split() не отработала
        if s.isdigit():
            result += sum(nums.append(s))
        else:
            done = True
    else:
        for c in s:
            if c.isdigit():
                nums.append(int(c))
            else:
                done = True
                break  # из данного цикла for
        result += sum(nums)
    print(result)
