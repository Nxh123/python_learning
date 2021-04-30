import json

file_name = 'favorite_number.json'
try:
    with open(file_name, "r") as f:
        number = json.load(f)
except FileNotFoundError:
    number = input('Please enter your favorite number: ')
    with open(file_name, "w") as f:
        json.dump(number, f)
else:
    print(f'Your favorite number is {number}')