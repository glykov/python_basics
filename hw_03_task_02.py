# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def one_line(first_name, last_name, year_birth, city_living, email, phone):
    '''Функция печатает данные пользователя в одной строке'''
    print(f"Имя: {first_name}, Фамилия: {last_name}, год рождения: {year_birth}, город проживания: {city_living}, email: {email}, телефон: {phone}")


one_line(last_name="Пушкин", first_name="Александр", phone="(812) 571-35-31",
         year_birth=1799, city_living="Санкт-Петербург", email='sunofrussianpoetry@yandex.ru')
