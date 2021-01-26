# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

hours_worked = 0
hourly_rate = 0
bonus = 0

if len(argv) != 4:
    print("Передано неверное количество параметров")
else:
    for arg in argv[1:]:
        param_name, val = arg.split('=')
        try:
            if param_name == '--hours' or param_name == '-h':
                hours_worked = float(val)
            elif param_name == '--rate' or param_name == '-r':
                hourly_rate = float(val)
            elif param_name == '--bonus' or param_name == '-b':
                bonus = float(val)
            else:
                print(f"Неизвестный параметр {param_name}")
        except ValueError:
            print(f"В параметре {param_name} переданы неверные данные")

    print(
        f"Зарплата составляет: {(hours_worked * hourly_rate + bonus):.2f} рублей")
