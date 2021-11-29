'''
try:
    do_smth()
except:
    do_another()

Type of Exceptions:
ImportError - неправильное обращение к библиотеке
IndexError - обращение к несуществующему элементу списка
NameError - неправильное имя переменной
TypeError - неправильно подобранный тип данных
ValueError - функция не получает аргумент правильного типа
ZeroDivisionError - деление на 0
'''

divider = int(input('Введите делитель: '))

try:  # попробовать сделать:
    print(182374 / divider)
except ArithmeticError:  # если случилась ошибка вычислений
    print('На 0 делить нельзя!')

print('hello')

