#Working with parts of a list
#slicing a list
players = ['messi', 'ronaldo', 'neymar', 'mbappe', 'bellingham', 'bruno']
print(players[0:3])
print(players[2:4])

print(players[:5])
print(players[3:])

print(players[-2:])

#looping through a slice
print('These players played for PSG:')
for player in players[0:3]:
    print(player.title())

#Copying lists
my_meals = ['banku', 'kenkey', 'fufu', 'fried rice', 'jollof']
friend_meals = my_meals[:]
print('My favourite meals are:')
print(my_meals)

print("\nMy friend's favourite meals are:")
print(friend_meals)

my_meals.append('indomie')
friend_meals.append('spagetti')
print("\nMy favourite meals are:")
print(my_meals)
print("\nMy friend's favourite meals are:")
print(friend_meals)

#Practice Exercise
animals = ['dog', 'lion', 'hawk', 'cat', 'goat', 'tiger','fish']
print('\nThe first 3 items in the list are:')
print(animals[0:3])
print('\nThese are the items in the middle of the list')
print(animals[3:5])
print('\nThese are the last items in the list')
print(animals[-3:])

places = ['egypt', 'china', 'brazil', 'tunisia', 'france']
far_places = places[0:4]
places.append('finland')
far_places.append('australia')

print('\nThese are places I would like to visit:')
print(places)
print('\nThese places are far from my home:')
print(far_places)

for animal in animals:
    print(animal.title())