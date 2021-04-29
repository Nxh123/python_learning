class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f'restaurant name:{self.restaurant_name}\ncuisine type:{self.cuisine_type}'
        )

    def open_restaurant(self):
        print('This restaurant is open.')


restaurant = Restaurant('沙县小吃', '小吃')
restaurant.describe_restaurant()
restaurant.open_restaurant()