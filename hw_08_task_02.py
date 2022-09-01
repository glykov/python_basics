# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZerroDivisionError(Exception):
    def __init__(self):
        self.text = "divisor must not be null"


try:
    dividend = int(input("Enter the first number: "))
    divisor = int(input("Enter the second number: "))

    if divisor == 0:
        raise MyZerroDivisionError()

except ValueError:
    print("You should enter two numbers")
except MyZerroDivisionError as mzd:
    print(mzd.text)
else:
    print(f"{dividend} / {divisor} = {dividend / divisor}")
