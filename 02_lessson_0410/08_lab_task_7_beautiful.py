from turtle import *

screen = Screen()
screen.bgcolor('black')

t = Turtle()
t.shape('turtle')
t.color('white')

size = 1

steps = 1
for i in range(1000):
    t.pensize(size)
    t.fd(steps)
    t.rt(10)
    steps += 0.5
    size += 0.5


done()
