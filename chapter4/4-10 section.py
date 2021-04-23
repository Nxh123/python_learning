cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)
print('The first three items in the list are:')
print(cubes[:3])
print('The items from the middle of the list are:')
print(cubes[4:7])
print('The last three items in the list are:')
print(cubes[-3:])