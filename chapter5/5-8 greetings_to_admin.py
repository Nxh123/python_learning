user_names = ['alice', 'bob', 'david', 'admin', 'eric']
for name in user_names:
    if name == 'admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print(f'Hello {name},thank you for logging in again.')