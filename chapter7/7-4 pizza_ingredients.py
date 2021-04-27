prompt = 'Input some pizza ingredients: '
ingredient = ''
while ingredient != 'quit':
    ingredient = input(prompt)
    if ingredient != 'quit':
        print(f'We will add {ingredient}')