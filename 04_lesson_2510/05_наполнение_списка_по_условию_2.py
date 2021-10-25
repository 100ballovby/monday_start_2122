import random as r  # импортирую библиотеку random

uniq_list = []  # создаю пустой список

while len(uniq_list) < 20:  # пока длина списка меньше 20
    rint = r.randint(1, 20)  # с каждым повторением генерирую число и сохраняю в переменной
    if rint not in uniq_list:  # число не находится в списке
        uniq_list.append(rint)  # добавить в список случайное число от 1 до 100

print(uniq_list)  # распечатать список