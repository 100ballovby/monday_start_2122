import os

path = '/Users/demidraksin/PycharmProjects/monday_start_2122/08_lesson_2911/test_directory'
entries = os.listdir(path)
entries.sort()

for file in entries:
    name, ext = os.path.splitext(os.path.join(path, file))
    print(name, ext)
    os.rename(os.path.join(path, file), name + '.txt')
