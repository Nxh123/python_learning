from random import choice

lottery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'g', 'd', 'f', 'h']
my_ticket = [4, 2, 6, 'a']
counter = 0
while True:
    counter += 1
    first_up = choice(lottery)
    second_up = choice(lottery)
    third_up = choice(lottery)
    forth_up = choice(lottery)
    if first_up not in my_ticket:
        continue
    elif second_up not in my_ticket:
        continue
    elif third_up not in my_ticket:
        continue
    elif forth_up not in my_ticket:
        continue
    else:
        break

print(f'You win the pirze in {counter} times.')
