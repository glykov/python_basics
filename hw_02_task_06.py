# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

products = []
analytics = {'название': [], 'цена': [], 'количество': [], 'ед': []}
product_qty = int(input("Какое количество товаров необходимо ввести? "))

for i in range(product_qty):
    item_name = input('Введите название товара: ')
    item_price = float(input('Ведите цену товара: '))
    item_qty = int(input('Введите количество товара: '))
    unit_measurement = input('Введите единицы измерения товара: ')
    products.append((i + 1, {'название': item_name, 'цена': item_price,
                             'количество': item_qty, 'ед': unit_measurement},))
    # учитывая, что в примере словаря из задания "шт." содержатся в единственном числе
    # принято допущение, что "статьи" словаря аналитики не содержит дублирующихся значений
    if item_name not in analytics['название']:
        analytics['название'].append(item_name)
    if item_price not in analytics['цена']:
        analytics['цена'].append(item_price)
    if item_qty not in analytics['количество']:
        analytics['количество'].append(item_qty)
    if unit_measurement not in analytics['ед']:
        analytics['ед'].append(unit_measurement)

# Проверочный вывод
print('\nВведены следующие товары')
for item in products:
    print(f"{item[0]}. название: {item[1]['название']}, цена: {item[1]['цена']}, количество: {item[1]['количество']}, ед: {item[1]['ед']}")

# Печатаем аналитику
print('\nСобраны следующие аналитические данные о товарах:')
for key, value in analytics.items():
    print(f'{key}: ', end='')
    for i in value:
        print(f'{i}, ', end='')
    print()
