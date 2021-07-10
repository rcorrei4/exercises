class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = str(restaurant_name)
        self.cuisine_type = str(cuisine_type)

    def describe_restaurant(self):
        print('\nRestaurant:', self.restaurant_name, 
              '\nCuisine Type:', self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant is open!')

restaurant = Restaurant('Rei do Mate', 'Bebidas')

print('\n' + restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

