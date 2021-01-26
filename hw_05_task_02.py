# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
# Используем файл, созданный в звдвнии 1 :-)

with open("task_01.txt", "r", encoding="utf8") as infile:
    data = infile.readlines()
    print(f"Количество строк в файле: {len(data)}")
    for i in range(len(data)):
        words = len(data[i].split())
        print(f"Строка {i + 1} содержит {words} слов(а)")
