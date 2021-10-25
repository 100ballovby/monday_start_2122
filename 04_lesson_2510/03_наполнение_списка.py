import random as r  # импортирую библиотеку random

r_list = []  # создаю пустой список

for i in range(30):  # повторять 30 раз
    r_list.append(r.randint(1, 100))  # добавить в список случайное число от 1 до 100

print(r_list)  # распечатать список
