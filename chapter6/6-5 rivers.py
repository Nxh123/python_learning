rivers = {
    'nile': 'egypt',
    'yellow river': 'china',
    'mississippi river': 'america',
}
for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())