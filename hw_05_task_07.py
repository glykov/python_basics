# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь(со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

companies = {}
average_profit = 0
number_companies = 0

with open('text_7.txt', 'r', encoding='utf8') as fp:
    for line in fp:
        elements = line.split()
        profit = float(elements[2]) - float(elements[3])
        companies[elements[0]] = profit
        if profit > 0:
            average_profit += profit
            number_companies += 1

data = [companies, {"average_profit": average_profit / number_companies}]

json.dump(data, fp=open('task_07.json', 'w',
                        encoding='utf8'), ensure_ascii=False, indent=4)

print(open('task_07.json', 'r', encoding='utf8').read())
