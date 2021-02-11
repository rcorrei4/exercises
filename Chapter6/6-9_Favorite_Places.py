favorite_places = {'ricardo': ['australia', 'usa', 'united kingdom'],
    'fernanda': ['south korea', 'usa'], 'karla': ['france', 'italy']
    }

for name, places in favorite_places.items():
    print('\n', name.title() + ':')
    for place in places:
        print('\t', place.title())