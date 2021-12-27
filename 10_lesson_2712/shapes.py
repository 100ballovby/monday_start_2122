def draw_square(turtle, x, y, size, color='black', side=50):
    turtle.up()  # поднимаю перо (перестаю рисовать)
    turtle.goto(x, y)  # перехожу в нужные координаты
    turtle.pensize(size)  # размер пера
    turtle.color(color)  # цвет пера черепашки
    turtle.down()  # опускаю перо (начать рисовать)

    for i in range(4):
        turtle.fd(side)  # иду вперед на количество шагов side
        turtle.rt(90)  # поворачиваю вправо на 90 градусов

    turtle.up()
    return None


def draw_triangle(turtle, x, y, size, color='black', side=50):
    turtle.up()  # поднимаю перо (перестаю рисовать)
    turtle.goto(x, y)  # перехожу в нужные координаты
    turtle.pensize(size)  # размер пера
    turtle.color(color)  # цвет пера черепашки
    turtle.down()  # опускаю перо (начать рисовать)

    for i in range(3):
        turtle.fd(side)  # иду вперед на количество шагов side
        turtle.lt(120)  # поворачиваю вправо на 90 градусов

    turtle.up()
    return None


def draw_star(turtle, x, y, size, color='black', side=50):
    turtle.up()  # поднимаю перо (перестаю рисовать)
    turtle.goto(x, y)  # перехожу в нужные координаты
    turtle.pensize(size)  # размер пера
    turtle.color(color)  # цвет пера черепашки
    turtle.down()  # опускаю перо (начать рисовать)

    for i in range(5):
        turtle.fd(side)  # иду вперед на количество шагов side
        turtle.rt(144)  # поворачиваю вправо на 90 градусов

    turtle.up()
    return None


def x_angle(turtle, x, y, size, corners, color='black', side=50):
    turtle.up()  # поднимаю перо (перестаю рисовать)
    turtle.goto(x, y)  # перехожу в нужные координаты
    turtle.pensize(size)  # размер пера
    turtle.color(color)  # цвет пера черепашки
    turtle.down()  # опускаю перо (начать рисовать)

    if corners >= 3:
        pass
    else:
        corners = 3
        print('Многоугольников меньше 3 углов не бывает!')

    for i in range(corners):
        turtle.fd(side)  # иду вперед на количество шагов side
        turtle.lt(360 / corners)  # поворачиваю вправо на 90 градусов

    turtle.up()
    return None
