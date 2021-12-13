def EmployeeFee(money: float) -> float:
    fee = 0
    for week in range(1, 53):
        fee += money
        print(f'Неделя №{week}, зарплата: {fee}')
    return fee

fee = 400
res = EmployeeFee(fee)


