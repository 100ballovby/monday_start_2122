def taxes(revenue: float, rate: int, signs: int) -> float:
    p = rate / 100  # перевожу ставку в процентное значение (дробь)
    res = round(revenue * p, signs)  # считаю итоговый налог и округляю до <sign> знаков после запятой
    return res

money = float(input('Введите выручку: '))
tax = int(input('Введите ставку налога: '))
result = taxes(money, tax, 4)
print(f'Сумма налога в этом квартале {result} руб.')
