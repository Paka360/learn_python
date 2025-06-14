#intro to If Statements
cars = ['audi', 'toyota', 'bmw', 'rolls_royce', 'bugatti']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

destination = 'Kumasi'
if destination != 'Accra':
    print('You are going the wrong way.')

answer = 45
if answer != 50:
    print('Wrong answer. Please try again!')

age = 24
if age < 30:
    print ('\nYou are young')
if age > 30:
    print('You are old')

#checking multiple conditions 
#Using 'and' to check multiple conditions
age_1 = 24
age_2 = 21
if age_1 > 30 and age_2 > 30:
    print('false')
if age_1 < 30 and age_2 < 30:
    print('true')
if (age_1 < 30) and (age_2 > 30):
    print('false')

#Using 'or' to check multiple conditions
if age_1 > 30 or age_2 > 30:
    print('false')
if age_1 < 30 or age_2 < 30:
    print('\nTrue')
if age_1 < 30 or age_2 > 30:
    print('True')

#checking for values in a list
destination = ['accra', 'kumasi', 'tamale', 'kasoa', 'ho']
location = 'accra'
if location in destination:
    print ('\nFinally we have arrived at '+ location.title())

location = 'amasaman'
if location not in destination:
    print('\nThis is '+location.title()+ ' we have not arrived yet.')


#Boolleon Expresssions 
game_active = True
Can_sing = False

#Practice Exercise
car = 'bugatti'
print("Is car == 'bugatti'? I predict true.")
print (car == 'bugatti')

print("\nIs car == 'toyota'? I vote False.")
print(car == 'toyota')

