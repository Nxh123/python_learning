favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
names = ['jen', 'alice', 'bob', 'sarah', 'eric']
for name in names:
    if name in favorite_languages.keys():
        print('Thank you!')
    else:
        print(f'{name.title()},please take our poll!')