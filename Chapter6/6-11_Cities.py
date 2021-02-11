cities = {
    'new york': {
        'country': 'usa',
        'population': '8 million',
        'fact': 'More than 800 languages are spoken in New York City.'
        },
        
    'são paulo': {
        'country': 'brazil',
        'population': '12 million',
        'fact': 'São Paulo has the 10º biggest PIB in the world.',
        },
    
    'buenos aires': {
        'country': 'argentina',
        'population': '2.8 million',
        'fact': 'Its center is the Plaza de Mayo.'
    }}

for cities_key, city_info in cities.items():
    print('\nCity:', cities_key.title())
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print('\tCountry:', country.title())
    print('\tPopulation:', population.title())
    print('\tFact:', fact)

