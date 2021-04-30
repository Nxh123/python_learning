while True:
    print('\nPlease enter two numbers\n(Enter "q" to exit.)')
    numbers_1 = input('first number: ')
    if numbers_1 == 'q':
        break
    numbers_2 = input('second number: ')
    if numbers_2 == 'q':
        break
    try:
        sum = int(numbers_1) + int(numbers_2)
    except ValueError:
        print('Please enter numbers')
    else:
        print(sum)