from random import randint


class Die:
    def __init__(self, slides=6):
        self.slides = slides

    def roll_die(self):
        number = randint(1, self.slides)
        print(number)


die_1 = Die()
for i in range(10):
    die_1.roll_die()

die_2 = Die(slides=10)
for i in range(10):
    die_2.roll_die()

die_3 = Die(slides=20)
for i in range(10):
    die_3.roll_die()