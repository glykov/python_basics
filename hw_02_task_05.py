# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

rating = []

while True:
    item = input(
        'Ведите целое число (для окончания введите любой нечисловой символ): ')
    if not item.isdigit():
        break
    item = int(item)
    # вставка первого элемента в список
    if len(rating) == 0:
        rating.append(item)
    else:
        done = False
        for i in range(len(rating)):
            if item > rating[i]:
                rating.insert(i, item)
                done = True
                break
        if not done:
            rating.append(item)

print('\nРейтинг: ')
for n in rating:
    print(n, end=' ')
print()
