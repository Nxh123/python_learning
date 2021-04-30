while True:
    reason = input(
        'Please tell me why you like programming(Enter "q" to exit.): ')
    if reason == 'q':
        break
    else:
        with open('reasons.txt', 'a') as file_object:
            file_object.write(reason)