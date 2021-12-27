import random as r
from shapes import x_angle
from turtle import *

t = Turtle()
t.shape('turtle')
colors = ['red', 'orange', 'yellow', 'green', 'cyan',
          'blue', 'purple', 'pink', 'violet',
          'green yellow', 'plum']

for shape in range(8):
    x = r.randint(-380, 380)
    y = r.randint(-380, 380)
    corners = r.randint(3, 9)
    col = r.choice(colors)  # достаю случайное значение из colors
    width = r.randint(30, 150)

    t.begin_fill()
    x_angle(t, x, y, 6, corners, col, width)
    t.end_fill()

done()
