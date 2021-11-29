import os

entries = os.listdir('/Users/demidraksin/PycharmProjects/monday_start_2122/08_lesson_2911')

# вывести названия объектов, которые являются файлами
for file in entries:
    if os.path.isfile(file):
        print(f'{file} - is file!')
