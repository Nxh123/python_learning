class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f'restaurant name:{self.restaurant_name}\ncuisine type:{self.cuisine_type}'
        )

    def open_restaurant(self):
        print('This restaurant is open.')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('沙县小吃', '小吃')
print(f'There are {restaurant.number_served} people in this restaurant.')
restaurant.number_served = 10
print(f'There are {restaurant.number_served} people in this restaurant.')
restaurant.set_number_served(32)
print(f'There are {restaurant.number_served} people in this restaurant.')
restaurant.increment_number_served(43)
print(f'There are {restaurant.number_served} people in this restaurant.')
