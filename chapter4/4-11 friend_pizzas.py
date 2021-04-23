pizzas = ['apple pizza', 'chicken pizza', 'beef pizza']
friend_pizzas = pizzas[:]
pizzas.append('orange pizza')
friend_pizzas.append('banana pizza')
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)