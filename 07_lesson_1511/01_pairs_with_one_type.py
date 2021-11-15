favorites_langs = {
    'Jen': 'c++',
    'Sarah': 'c',
    'Lenny': 'python',
    'phil': 'java',
}

# перебор ключей словаря
for key in favorites_langs.keys():  # для каждого ключа в словаре
    print(f'Key: "{key}";')

# перебор значений словаря
for value in favorites_langs.values():  # для каждого значения в словаре
    print(f'Value: "{value}";')

# перебор пар
for key, value in favorites_langs.items():  # перебор всех пар словаря
    print(f"{key.capitalize()}'s favorite language is {value.capitalize()}.")

# упорядоченный перебор ключей в словаре
for name in sorted(favorites_langs.keys()):
    print(f'Hello, {name}! Good to see you!')
