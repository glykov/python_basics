# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

in_lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

out_lst = [in_lst[x]
           for x in range(1, len(in_lst)) if in_lst[x] > in_lst[x - 1]]

print(in_lst)
print(out_lst)