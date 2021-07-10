def city_country(city, country):
    ccountry = city + ', ' + country
    return ccountry.title()

spbr = city_country('São Paulo', 'Brazil')
print(spbr)

nyus = city_country('New York', 'USA')
print(nyus)

baar = city_country('Buenos Aires', 'Argentina')
print(baar)
