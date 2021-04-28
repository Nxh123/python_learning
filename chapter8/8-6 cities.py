def city_country(city, country):
    message = f'{city.title()},{country.title()}'
    return message


city1 = city_country('Beijing', 'China')
print(city1)
city2 = city_country('Shanghai', 'China')
print(city2)
city3 = city_country('Tokyo', 'Japan')
print(city3)