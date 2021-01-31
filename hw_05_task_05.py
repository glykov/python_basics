# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

file_name = 'task_05.txt'

with open(file_name, 'w') as fout:
    for i in range(10):
        print(randint(1, 100), end=" ", file=fout)

with open(file_name, 'r') as fin:
    data = map(int, fin.read().split())
    print(sum(data))
