# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

once = input()
twice = once * 2
thrice = once * 3

sum = int(once) + int(twice) + int(thrice)
print(sum)
