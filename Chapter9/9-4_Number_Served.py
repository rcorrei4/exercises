class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = str(restaurant_name)
        self.cuisine_type = str(cuisine_type)
        self.number_served = 0

    def describe_restaurant(self):
        print('\nRestaurant:', self.restaurant_name, 
              '\nCuisine Type:', self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant is open!')

    def print_number_served(self):
        print(f'The number of customers served is {self.number_served}.')

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, increment_customers):
        self.number_served += increment_customers

        

restaurant = Restaurant('Rei do Mate', 'Bebidas')

print('\n' + restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.print_number_served()
restaurant.number_served = 20
restaurant.print_number_served()

restaurant.set_number_served(30)
restaurant.print_number_served()

restaurant.increment_number_served(10)
restaurant.print_number_served()

