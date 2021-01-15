# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

starting_distance = float(input('Введите стартовую дистанцию: '))
target_distance = float(input('Введите целевую дистанцию: '))

day = 1
distance = starting_distance

while distance < target_distance:
    print(f'{day}-й день: {distance:.2f}')
    day += 1
    distance *= 1.1

# распечатать дистанцию пробежки в последний день
print(f'{day}-й день: {distance:.2f}')
print(f'на {day}-й день спортсмен достиг результата — не менее {target_distance} км')