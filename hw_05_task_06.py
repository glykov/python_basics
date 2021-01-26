# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re

# Решение без регулярных выражений
education = {}

with open('text_6.txt', 'r', encoding='utf8') as fin:
    for line in fin:
        words = line.split()
        hours = 0
        for i in range(1, 4):
            if words[i][0].isdigit():
                pos = words[i].find('(')
                hours += int(words[i][:pos])
        education[words[0][:-1]] = hours

for k, v in education.items():
    print(f'{k}: {v} часов')
print()

# Решение с регулярными выражениями
education_rx = {}
num_rx = re.compile(r'\d+')

with open('text_6.txt', 'r', encoding='utf8') as fin:
    for line in fin:
        hours = sum(map(int, num_rx.findall(line)))
        subject = line[:line.find(':')]
        education_rx[subject] = hours

for k, v in education_rx.items():
    print(f'{k}: {v} часов')
print()
