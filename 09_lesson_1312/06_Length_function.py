"""
Разработать функцию Length(), которая вычсиляет длину
отрезка, образованного точками x1, y1, x2, y2
"""


def Length(x1: float, y1: float, x2: float, y2: float) -> float:
    from math import sqrt
    len = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    return len

x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
res = Length(x1, y1, x2, y2)
print(round(res, 5))
