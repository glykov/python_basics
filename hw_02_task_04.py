# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

string_list = input('Введите строку: ').split()

print('\nСтрока содержит следующие слова:')
for i, s in enumerate(string_list, 1):
    print(f'{i}: {s[:10]}')
