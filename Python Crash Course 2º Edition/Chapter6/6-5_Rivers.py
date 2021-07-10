rivers = {'tigris': 'iraq', 'amazon': 'brazil', 'ganges': 'india'}

for river, country in rivers.items():
    print(f'The {river.title()} river runs in {country.title()}.')

print('\nRivers:')

for river in rivers.keys():
    print(f'{river.title()} river')

print('\nCountries:')

for country in rivers.values():
    print(f'{country.title()}')