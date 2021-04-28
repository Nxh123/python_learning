def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Xinahn', 'Niu', age=21, birthday='May 2nd')
print(user_profile)