# параллельно с открытием(файл, режим) как f
with open('text.txt', 'r') as f:
    print(f.read())
'''
r - чтение 
w - запись 
w+ - чтение/запись 
a - append (добавление)
'''

with open('text.txt', 'w+') as f:
    text = 'Это новый текст для записи в файл'
    f.write(text)
    print(f.read())

with open('text.txt', 'a') as f:
    text = '\nменя добавили к старому тексту'
    f.write(text)
