# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
from random import randint

direction = ['right', 'left']


class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color.title()} {self.name} is going forward")

    def stop(self):
        print(f"{self.name} has stopped")

    def turn(self, direction):
        print(f"{self.name} turns {direction}")

    def show_speed(self):
        print(f"{self.name} has speed {self.speed} mph")


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        print(f"{self.speed} is too high for {self.name}" if self.speed >
              self.speed_limit else super().show_speed())


class SportCar(Car):
    speed_limit = 150


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        print(f"{self.speed} is too high for {self.name}" if self.speed >
              self.speed_limit else super().show_speed())


class PoliceCar(Car):
    speed_limit = 200


pc = PoliceCar(120, "white", "Dodge Charger", True)
print("It is police car" if pc.is_police else "It is not police car")
pc.go()
pc.show_speed()
pc.turn(direction[randint(0, 1)])

print()

sc = SportCar(200, "yellow", "Ford Mustang")
print("It is police car" if sc.is_police else "It is not police car")
sc.go()
sc.show_speed()

print()

wc = WorkCar(50, "brown", "Ford Transit")
wc.go()
wc.show_speed()
wc.stop()

print()

tc = TownCar(50, "red", "Toyota Corolla")
tc.go()
tc.turn(direction[randint(0, 1)])
tc.show_speed()
# при вызове super().show_speed() выводит сообщение о скорости, и еще None.Почему?
