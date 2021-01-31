# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep
from colorama import init, Fore

init()
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN]


class TrafficLight():
    __color = ['red', 'yellow', 'green']

    def running(self):
        for i, j in enumerate([7, 2, 7]):
            print(colors[i] + self.__color[i])
            sleep(j)


tl = TrafficLight()
tl.running()
