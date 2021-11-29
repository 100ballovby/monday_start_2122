'''Необходимо попросить пользователя наполнить список числами вручную.
При этом проверять, чтобы это точно были числа.
'''
numbers = []
length = int(input('Введите длину списка: '))

while len(numbers) < length:
    try:
        n = int(input('Введите число: '))
        numbers.append(n)
    except ValueError:
        print('Это не число!')

print(numbers)


