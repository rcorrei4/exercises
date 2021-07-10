class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = str(restaurant_name)
        self.cuisine_type = str(cuisine_type)

    def describe_restaurant(self):
        print('\nRestaurant:', self.restaurant_name, 
              '\nCuisine Type:', self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant is open!')

restaurant_reidomate = Restaurant('Rei do Mate', 'Bebidas')

print('\n' + restaurant_reidomate.restaurant_name)
print(restaurant_reidomate.cuisine_type)

restaurant_reidomate.describe_restaurant()
restaurant_reidomate.open_restaurant()

restaurant_outback = Restaurant('Outback', 'Grill')
restaurant_dominos = Restaurant('Dominos', 'Pizza')

restaurant_outback.describe_restaurant()
restaurant_dominos.describe_restaurant()