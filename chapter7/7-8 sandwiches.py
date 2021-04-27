sandwich_orders = ['tuna sandwich', 'vegetable sandwich', 'chicken sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich}')
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(f'{sandwich} was finished.')