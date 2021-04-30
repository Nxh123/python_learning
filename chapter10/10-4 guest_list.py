while True:
    name = input('Please input your name(Enter "q" to exit.): ')
    if name == 'q':
        break
    else:
        print(f'Welcome {name.title()}')
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f'{name.title()} visited.\n')