cities = {
    'Beijing': {
        'country': 'china',
        'population': '21 millions',
        'fact': 'Beijing is the captial of China.'
    },
    'Tokyo': {
        'country': 'japan',
        'population': '9 millions',
        'fact': 'Tokyo is the captial of Japan',
    },
    'Hongkong': {
        'country': 'china',
        'population': '7 millions',
        'fact': 'Hongkong is a Special Administrative Region of China',
    },
}
for city, info in cities.items():
    print(city)
    print(f"{info['country']}\n{info['population']}\n{info['fact']}")
