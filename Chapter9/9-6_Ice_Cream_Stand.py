class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = str(restaurant_name)
        self.cuisine_type = str(cuisine_type)

    def describe_restaurant(self):
        print('\nRestaurant:', self.restaurant_name, 
              '\nCuisine Type:', self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant is open!')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

Sorvete = IceCreamStand('gelado', 'icecream', ['maracujá', 'manga', 'chocolate'])
Sorvete.display_flavors()
