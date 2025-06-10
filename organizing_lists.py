#Organizing lists
#the sort function allows for the order of a list to be changed permanently
#Using sort method to organize lists(alphabetical order)
cars = ['bmw', 'toyota', 'rolls_royce', 'audi', 'subaru']
cars.sort()
print (cars)

#sorting in reverse alphabetical order
cars = ['bmw', 'toyota', 'rolls_royce', 'audi', 'subaru']
cars.sort(reverse=True)
print (cars)

#the sorted function allows for the order to be changed temporarily
subjects = ['maths', 'english', 'social_studies', 'french']
print ('Here is the original list')
print(subjects)

print('\nHere is the ordered list')
print(sorted(subjects))

print('\nHere is the original list again')
print(subjects)

#printing a list in reverse order
meals = ['rice', 'soup', 'banku', 'salad']
print (meals)

meals.reverse()
print (meals)

#finding length of a list
players = ['Mbappe', 'Messi', 'Ronaldo', 'Modric', 'Bellingham']
len(players)
print (len(players))

#Practice exercise
places = ['fuji', 'london', 'new_york', 'luthon', 'cairo']
print(places)
print(sorted(places))
print(places)

print(sorted(places, reverse=True))
print (places)

places.reverse()
print (places)
places.reverse()
print(places)

places.sort()
print(places)
places.sort(reverse=True)
print(places)

guests = ['stephen', 'micheal', 'kelvin', 'laura', 'kekeli', 'princess', 'lansford', 'enko']
number = str(len(guests))
message = 'I have decided to throw a party this Saturday. I will need enough food and drinks for '+ number +' people.'
print(message)
