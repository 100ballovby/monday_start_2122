import os

try:
    os.mkdir('test_directory')
except FileExistsError:
    print('Папка уже создана!')

path = '/Users/demidraksin/PycharmProjects/monday_start_2122/08_lesson_2911/test_directory'
try:
    for i in range(50):
        with open(os.path.join(path, f'file_{i}.py'), 'w') as f:
            f.write(f'print("Hello, World!")\nprint("file {i}")')
except:
    pass


