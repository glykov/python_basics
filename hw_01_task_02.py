# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
seconds = int(input())

# выделяем часы
hours = seconds // 3600
seconds = seconds % 3600

# выделяем минуты
minutes = seconds // 60
seconds = seconds % 60

print(f'{hours:02}:{minutes:02}:{seconds:02}')
