current_users = ['alice', 'bob', 'david', 'eric', 'frank']
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())
new_users = ['alice', 'bob', 'hans', 'jack', 'lambert']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('Please put in another name.')
    else:
        print('This name has not been used yet.')