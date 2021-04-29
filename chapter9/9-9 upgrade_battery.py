class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge')

    def upgarde_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


battery = Battery()
battery.get_range()
battery.upgarde_battery()
battery.get_range()
