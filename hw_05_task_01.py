# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

prompt = "Введите данные. Для выхода дважды нажмите Enetr: "
data = "@"

with open("task_01.txt", "w", encoding="utf8") as outfile:
    while data != "":
        data = input(prompt)
        print(data, file=outfile)
