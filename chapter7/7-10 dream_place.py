dream_places = {}
active = True
while active:
    name = input('\nWhat is your name? ')
    palce = input('\nWhat is your dream place? ')
    dream_places[name] = palce
    repeat = input(
        '\nWould you like to let another person respond(yes or no)? ')
    if repeat == 'no':
        active = False
print('\n--- Results ---')
for name, palce in dream_places.items():
    print(f'{name.title()} would like to visit {palce.title()}')