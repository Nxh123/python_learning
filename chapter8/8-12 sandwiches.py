def make_sandwiches(*args):
    print('\nYour sandwich will be made by:')
    for arg in args:
        print(f'- {arg}')


make_sandwiches('apple', 'banana')
make_sandwiches('chicken', 'beef')
make_sandwiches('vegetable')