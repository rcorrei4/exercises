favorite_numbers = {'erick': [8, 10], 'igor': [1, 0], 'luan': [7, 4],
                    'eduardo': [3, 100], 'ricardo': [2, 666]
                    }

for name, numbers in favorite_numbers.items():
    print('\n', name.title() + ':')
    for number in numbers:
        print('\t', number)
