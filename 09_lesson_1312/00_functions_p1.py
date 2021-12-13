def yourName() -> str:  # определение функции
    print('Привет!')
    name = input('Как тебя зовут? ')
    return name  # возврат значения


def sayHello(name: str) -> None:  # name - это строчный параметр функции
    print(f'Привет, {name}!')
    # если не написать return, python подставит его автоматически и будет возвращать тип данных None

# yourName()  вызов функции
txt = yourName()  # присваиваю переменной результат функции
sayHello(txt)  # передача аргумента функции

