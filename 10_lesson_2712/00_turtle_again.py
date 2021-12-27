import shapes as sh
from turtle import *

t = Turtle()

for i in range(7):
    sh.draw_square(t, i * 20, 40, 4, 'pink', 20)
for i in range(7):
    sh.draw_square(t, 140, i * 20, 4, 'pink', 20)
#draw_square(t, -200, -150, 5, 'red', 100)

sh.draw_star(t, 325, -325, 6, 'yellow', 100)

done()
