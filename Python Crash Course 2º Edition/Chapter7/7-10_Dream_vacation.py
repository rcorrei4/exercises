dream_vacations = {}

polling_active = True

while polling_active:
    name = input('Enter your name: ')
    place = input('What place would make your dream vacation true?')

    dream_vacations[name] = place
    
    repet = input('Another person want to make the poll? (yes/no)  ')
    
    if repet == 'no':
        polling_active = False

print('\nPoll results:  ')
for name, place in dream_vacations.items():
    print(f'\n{name.title()} would like to go to {place.title()}')
    print('To make his dream vacation true.')
