numbers = []
for i in range(1, 101):
    numbers.append(i)

low = 0
high = len(numbers)
mid = len(numbers) // 2

for i in range(7):
    n = input(f'Ты загадал число: {numbers[mid]}?')
    if n == 'нет':
        q = input('Твое число больше или меньше? (</>)')
        if q == '<':
            high = mid - 1  # отсекаю правую часть массива
        else:
            low = mid + 1  # отсекаю левую часть массива
    elif n == 'да':
        break
    mid = (low + high) // 2

if n == 'да':
    print('Ура! Я угадал!')
else:
    print('Не получилось')





