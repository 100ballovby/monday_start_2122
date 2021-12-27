"""Создайте функцию, которая рисует
паука с заданным количеством лап"""
from turtle import *


def draw_spider(turtle, x, y, size, n, color='black', side=50):
    turtle.up()  # поднимаю перо (перестаю рисовать)
    turtle.goto(x, y)  # перехожу в нужные координаты
    turtle.pensize(size)  # размер пера
    turtle.color(color)  # цвет пера черепашки
    turtle.down()  # опускаю перо (начать рисовать)

    for i in range(n):
        turtle.fd(side)  # иду вперед на количество шагов side
        turtle.bk(side)  # иду назад на количество шагов side
        turtle.rt(360 / n)  # поворачиваю вправо на 90 градусов

    turtle.up()
    return None

t = Turtle()
draw_spider(t, 100, -100, 4, 15, 'pink', 100)

done()