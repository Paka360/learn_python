#intro to dictionaries
alien_0 = {'color': 'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print ('You just earned '+ str(new_points) + ' points!')

#Adding new key-value pairs
alien_0 ={'color':'red', 'points':5}
print(alien_0)
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

#Starting with an empty dictionary
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = 3
print(alien_1)

#Modifying values in dictionaries
alien_2 = {'color':'gray'}
print("The alien is "+ alien_2['color']+'.')

alien_2['color'] = 'yellow'
print("The alien is now " + alien_2['color'] +'.\n')

alien_3 = {'x-position':0, 'y-position':25, 'speed':'medium'}
print("Original x-position: " + str(alien_3['x-position']))

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_3['x-position'] = alien_3['x-position'] + x_increment
print("New position: "+ str(alien_3['x-position']))