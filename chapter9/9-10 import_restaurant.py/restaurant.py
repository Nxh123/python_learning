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