
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# print(list(zip(names, heros)))

# I want a dict{'name":'hero'} for each name, hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for  name, hero in zip(names, heros)}
# print(my_dict)

# If name not equal 'Peter'
my_dict = {name: hero for  name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)