def taxes(revenue: float, rate: int, signs: int) -> float:
    p = rate / 100  # перевожу ставку в процентное значение (дробь)
    res = round(revenue * p, signs)  # считаю итоговый налог и округляю до <sign> знаков после запятой
    return res

clients = [(4563, 13), (12789.3, 8), (121578.23, 11),
           (56789.7, 16), (876.35, 7), (3098.22, 5)]

for client in clients:
    res = taxes(client[0], client[1], 2)
    print(f'Сумма налога: {res} руб.')

