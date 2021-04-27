prompt = '\nHow old are you? '
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('Free.')
    elif age <= 12:
        print('10 dollars.')
    elif age > 12:
        print('15 dollars.')