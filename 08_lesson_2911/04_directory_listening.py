import os

entries = os.listdir('/Users/demidraksin/PycharmProjects/monday_start_2122/08_lesson_2911')
print(entries)

for file in entries:  # для каждого файла в папке
    with open(file, 'r') as f:
        print(f.read(), '\n\n\n')
