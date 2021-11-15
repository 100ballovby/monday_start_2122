phone = {
    'mom': {'phone': '+375291234567',
            'email': 'mom@gmail.com',
            'birthdate': '11.11.2011'
            },
    'father': {'phone': ['+375297654321',
                         '+375331234567',
                         '+375447894522'],
               'email': 'father@gmail.com',
               'birthdate': '13.11.2011'
               },
    'sister': {'phone': '+3755673241',
               'email': 'sis@gmail.com',
               'birthdate': '16.09.2015'
               },
}

print(phone)
print(phone['father'])
print(phone['father']['phone'])
print(phone['father']['phone'][1])

