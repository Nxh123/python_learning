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


restaurant1 = Restaurant('沙县小吃', '小吃')
restaurant2 = Restaurant('过桥米线', '米线')
restaurant3 = Restaurant('肥叔锅贴', '锅贴')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()