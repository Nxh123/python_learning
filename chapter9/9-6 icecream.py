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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['apple', 'banana', 'orange']

    def show_icecream(self):
        print(self.flavors)


icecramstand = IceCreamStand('ice', 'icecream')
icecramstand.show_icecream()
