from turtle import *

t = Turtle()
t.shape('turtle')

steps = 1
for i in range(1000):
    t.fd(steps)
    t.rt(10)
    steps += 0.5

done()
