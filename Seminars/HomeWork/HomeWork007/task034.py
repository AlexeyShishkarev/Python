# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам


inp = input('Введите кричалку: ')
inp += ' '



list_1 = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']

list_count = []

count = 0

for i in inp:
    if i in list_1:
        count += 1
    elif i not in list_1 and i != ' ':
        continue
    else:
        if i == ' ' and count != 0:
            list_count.append(count)
        count = 0

list_count = set(list_count)

if len(list_count) > 1:
    print('Пам парам')
else:
    print('Парам пам-пам')

