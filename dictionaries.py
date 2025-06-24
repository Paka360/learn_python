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

#Removing Key-Value Pairs
alien_0 ={'color':'red', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)

#A Dictionary of similar objects
favourite_languages = {
    'john':'python',
    'stella':'html', 
    'phil':'c',
    'graham':'css'
    }
print("Phil's favourite programming language is " + 
      favourite_languages['phil'].title() +'.')


#Practice Exercise
new_friend = {
    'firstname':'stephen', 
    'lastname':'lang', 
    'favourite_food':'eba', 
    'age': 18, 
    'city':'hong kong'
    }
print(new_friend['firstname'].title())
print(new_friend['lastname'].title())
print(new_friend['age'])
print(new_friend['city'].title())
print(new_friend['favourite_food'].title())

names = ['jane', 'hank', 'mike', 'fred', 'hannah']
fav_numbers = {'jane':23, 'hank':4, 'mike':10, 'fred':100, 'hannah':44,}

print("Jane's favourite number is " + str(fav_numbers['jane']))
print("Hank's favourite number is " + str(fav_numbers['hank']))
print("Mike's favourite number is " + str(fav_numbers['mike']))
print("Hannah's favourite number is " + str(fav_numbers['hannah']))
print("Fred's favourite number is " + str(fav_numbers['fred']))

#looping through a dictionary
#looping through all key-value pairs

user_1 ={
    'firstname':'hannah',
    'lastname':'blay',
    'age':'17',
    'username':'ladyblay',
}
for key, value in user_1.items():
    print('\nkey: '+ key)
    print('value: '+ value)

for name, language in favourite_languages.items():
    print("\nname: "+ name.title())
    print("language: "+ language.upper())

#looping through all keys in a dictionary
for name in favourite_languages.keys():
    print('\n' + name.title())
for name in favourite_languages:
    print('\n' + name.title())

print('\n')

friends = ['stella', 'maria', 'ben', 'phil']
for name in favourite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(name.title()+ " your favourite programming language is "+
               favourite_languages[name].upper() + '.\n')

if 'eric' not in favourite_languages.keys():
    print("\nEric, please answer the question.\n")
    
#looping through keys in order
for name in sorted(favourite_languages.keys()):
    print(name.title() +", thank you for answering the questions.\n")

#looping through all values in a dictionary
fav_books ={
    'stella':'calculus',
    'amin':'forth wing',
    'claudia':'psycology of money',
    'sarkodie': 'elcetrical machines',
    'jesse':'calculus',
}
print('\nThe following books have been selected.')
for book in fav_books.values():
    print(book.title())

print('\n')
#the following lines ensures you do not have a repetitive list of items in your values when looping through them
for book in set(fav_books.values()):
    print(book.title())

#Practice Exercise
glossary = {
    'varaiable':'used for storing data',
    'str':'data type for storing texts',
    'int':'data type for storing numbers',
    'comments':'part of the code python ignores',
    'lists':'collection of items',
    'elements':'items in a list',
    'print':'gives you an output',
    'del':'removes items in your list permanently',
    'insert':'adds new items to a list',
    'pop':'lets you delete an item and still have access to it'
    }
for glo, meaning in glossary.items():
    print('\nglossary: ' + glo.title())
    print('meaning: ' + meaning)