# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

start = int(input("Введите начальное значение: "))
stop = int(input("Введите последнее число последовательности: "))
if start <= stop:
    step = 1
else:
    step = -1

for i in count(start, step):
    print(i, end=" ")
    if stop == start:
        break
    else:
        stop -= step

print('\n')

seq = input("Введите последовательность для повторения: ")
num = int(input("Введите необходимое количество повторений: "))

for i in cycle(seq):
    if num == 0:
        break
    else:
        print(i, end=" ")
        num -= 1

print()
