from random import randint


class Die:
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """摇骰子"""
        return randint(1, self.num_sides)
