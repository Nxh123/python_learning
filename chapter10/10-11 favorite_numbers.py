import json

number = input('Please enter your favorite number: ')
number = int(number)
with open('favorite_number.json', "w") as f:
    json.dump(number, f)

with open('favorite_number.json') as f:
    number_load = json.load(f)

print(f'I know your favorite number!It is {number_load}')