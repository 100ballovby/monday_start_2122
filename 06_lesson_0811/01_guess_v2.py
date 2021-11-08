import random as r

secret_num = r.randint(1, 100)
guessTaken = 0  # веду подсчет попыток пользователя угадать число
answer = None

name = input('Как тебя зовут? ')
print(f'Привет, {name}! Я загадал число от 1 до 100. Угадай его.')

while guessTaken <= 6 and answer != secret_num:
    guessTaken += 1
    answer = int(input('Введите число: '))

    if answer > secret_num:
        print('Слишком много!')
    elif answer < secret_num:
        print('Слишком мало!')

if answer == secret_num:
    print(f'Ты угадал за {guessTaken} шагов! Молодец!')
else:
    print(f'Попытки исчерпаны. Ты не угадал! Я загадывал число {secret_num}.')