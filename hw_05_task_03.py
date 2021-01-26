# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

employees = {}

with open("text_3.txt", "r", encoding="utf8") as infile:
    counter = 0
    for line in infile:
        name, salary = line.split()
        employees[name] = float(salary)

total = 0
poors = []
salaries = []

for name, salary in employees.items():
    total += salary
    salaries.append(salary)
    if salary < 20000:
        poors.append(name)

average = total / len(employees)
print(f"Средняя заработная плата составляет {average} у.е.")

median = 0
number_elements = len(salaries)
sorted_sal = sorted(salaries)
if number_elements % 2 == 0:
    median = (sorted_sal[number_elements // 2 - 1] +
              sorted_sal[number_elements // 2]) / 2
else:
    median = sorted_sal[number_elements // 2]
print(f"\nМедиана заработной платы составляет {median} у.е.")

print("\nСотрудники, зарабатывающие менее 20 000 у.е.:")
for emp in poors:
    print(emp)
