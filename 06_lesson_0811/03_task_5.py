n = input('Введите натуральное число: ')

count = 0
for i in n:
    if int(i) % 2 == 0 and int(i) != 0:
        count += 1

print(count)

