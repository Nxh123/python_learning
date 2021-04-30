def city_function(city, country, population=''):
    if population:
        string = f'{city.title()},{country.title()} - population {population}'
    else:
        string = f'{city.title()},{country.title()}'
    return string