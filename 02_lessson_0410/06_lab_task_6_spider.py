from turtle import *

t = Turtle()
t.shape('turtle')

n = int(input('Сколько лап у паука? '))
for i in range(n):
    t.fd(100)
    t.stamp()  # отпечаток черепашки
    t.bk(100)
    t.rt(360 / n)

done()
