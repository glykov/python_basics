# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_str):
        self.date = self.convert_date_str(date_str)

    @classmethod
    def convert_date_str(cls, date):
        date = [x for x in map(int, date.split('-'))]
        if Date.validate_date(*date):
            return date
        else:
            return []

    @staticmethod
    def validate_date(day, month, year):
        date_valid = False
        if year < 0:
            return date_valid
        if 1 <= day <= 31 and month in [1, 3, 5, 7, 8, 10, 12]:
            date_valid = True
        elif 1 <= day <= 30 and month in [4, 6, 9, 11]:
            date_valid = True
        elif 1 <= day <= 28 and not Date.is_leap_year(year):
            date_valid = True
        elif 1 <= day <= 29 and Date.is_leap_year(year):
            date_valid = True

        return date_valid

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


a = Date('18-05-2009')
print(a.date)
