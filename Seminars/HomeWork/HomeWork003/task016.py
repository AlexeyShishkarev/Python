# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

n = int(input('Введите размер массива: '))
list_1 = list()

for i in range(0, n):
    number = random.randint(0, 10)
    list_1.append(number)

print(list_1)

k = int(input('Введите число к для поиска: '))
print(list_1.count(k))



