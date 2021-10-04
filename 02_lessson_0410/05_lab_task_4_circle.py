from turtle import *

t = Turtle()
t.shape('turtle')

# TODO: нарисовать окружность
for i in range(72):
    t.fd(10)
    t.rt(5)

# НО! у черепашки есть встроенная функция circle(r), которая рисует окружность по нужному радиусу
t.color('cyan')
t.circle(70)
# можно еще нарисовать закрашенный круг, для этого есть функия .dot(r)
t.color('green')
t.dot(30)

done()
