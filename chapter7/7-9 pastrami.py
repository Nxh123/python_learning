sandwich_orders = [
    'tuna sandwich', 'pastrami sandwich', 'vegetable sandwich',
    'pastrami sandwich', 'chicken sandwich', 'pastrami sandwich'
]
finished_sandwiches = []
print('Pastrami Sandwiches were sold out.')
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich}')
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'{sandwich} was finished.')