# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел.


import random

print(list_1 := [random.randint(0, 2) for _ in range(10)])
list_2 = list()

for i in list_1:
    list_2 += {(i, list_1.count(i) // 2)}

list_2 = set(list_2)

list_2 = sorted(list(list_2))

print(list_2)

