from turtle import *

t = Turtle()
t.shape('turtle')

# TODO: нарисовать квадрат
for i in range(4):  # 4 раза сделать:
    t.fd(100)
    t.lt(90)

t.up()  # поднимаю перо (перестаю рисовать
t.goto(-200, 250)  # перемещу черепаху в другие координаты
t.down()  # опускаю (начинаю рисовать)

# TODO: нарисовать прямоугольник
for i in range(2):  # 4 раза сделать:
    t.fd(200)
    t.lt(90)
    t.fd(100)
    t.lt(90)

done()
