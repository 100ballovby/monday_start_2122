def multiply(a: int, b: int) -> int:
    return a * b


def addition(a: int, b: int) -> int:
    return a + b


def difference(a: int, b: int) -> int:
    return a - b


def divide(a: int, b: int) -> float or str:
    try:
        res = a / b
        return res
    except ArithmeticError:
        return 'Деление на 0 запрещено!'
