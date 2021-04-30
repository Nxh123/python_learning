print('\nPlease enter two numbers')
numbers_1 = input('first number: ')
numbers_2 = input('second number: ')
try:
    sum = int(numbers_1) + int(numbers_2)
except ValueError:
    print('Please enter numbers')
else:
    print(sum)