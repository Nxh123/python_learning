from random import choice

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'g', 'd', 'f', 'h']
first_up = choice(lottery)
second_up = choice(lottery)
third_up = choice(lottery)
forth_up = choice(lottery)
print(
    f'If your code includes {first_up} {second_up} {third_up} {forth_up},you win the prize.'
)
