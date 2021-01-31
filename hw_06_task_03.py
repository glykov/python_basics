# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, position, wage, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    _income = {}

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum([*self._income.values()])


pos = Position('Harry', 'Hacker', 'programmer', 5000, 200)
print(pos.name)
print(pos.surname)
print(pos.position)
for k, v in pos._income.items():
    print(f"{k}: {v}")
print(pos.get_full_name())
print(pos.get_total_income())
