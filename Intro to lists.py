#lists are a collection of items
bicycles = ['trek', 'bone crusher', 'redline', 'cannondale', 'specialized']
print (bicycles)

#Accessing elements of lists
print(bicycles[0])
#Accessing the last elements in a list
print(bicycles[-1])
print(bicycles[-2])

#Using individual values from a list
message = 'My first bicycle was a ' + bicycles[1].title() +'.'
print( message)

#Exercise
names = [ 'John' , 'Micheal' , 'Cletus' , 'Stephen', 'Laura' , 'Kekeli']
print (names[0].title())
print (names[1].title())
print (names[2].title())
print (names[3].title())
print (names[4].title())
print (names[5].title())

message1 = 'The name of my best friend is ' + names[0] +'.'
print (message1)
message1 = 'The name of my best friend is ' + names[1] +'.'
print (message1)
message1 = 'The name of my best friend is ' + names[2] +'.'
print (message1)
message1 = 'The name of my best friend is ' + names[3] +'.'
print (message1)
message1 = 'The name of my best friend is ' + names[4] +'.'
print (message1)
message1 = 'The name of my best friend is ' + names[5] +'.'
print (message1)

cars = ['Toyota', 'Hundai', 'Rolls Royce', 'Tesla']

message2 = 'I would like to own a '+ cars[-1].title() + ' one day.'
print (message2)
message2 = 'I would like to own a '+ cars[-2].title() + ' one day.'
print (message2)
message2 = 'I would like to own a '+ cars[-3].title() + ' one day.'
print (message2)
message2 = 'I would like to own a '+ cars[-4].title() + ' one day.'
print (message2)

#Modifying lists
meals = ['banku', 'rice', 'kenkey', 'fufu', 'yam']
print (meals)

meals[3] = 'tuozaafi'
print (meals)
 
#Adding elements to lists. Append method
meals = ['banku', 'rice', 'kenkey', 'fufu', 'yam']
print (meals)
meals.append('tuozaafi')
print (meals)

meals = []
meals.append('banku')
meals.append('kenkey')
meals.append('rice')
print (meals)

#Adding elements to lists. Insert method
names2 = ['ama', 'kojo', 'akosua']
names2.insert(0, 'kofi')
print (names2)

#Removing elements from lists
items = ['chair', 'table', 'shoe', 'book']
print (items)

del items[2]
print (items)

#Removing elements using pop() method
items = ['cup', 'box', 'slippers', 'pen']
print (items) 

popped_items = items.pop()
print (items)
print (popped_items)

subjects = ['maths', 'science', 'english', 'social studies']
print (subjects)
fav_subject = subjects.pop(1)
print (subjects)
print (fav_subject)
message3 = 'My favourite subject is ' + fav_subject + '.'
print ( message3)

#Removing elements by value
artists = ['Juice wrld', 'Post Malone', 'Eminen', 'Adele', 'Rihanna']
print (artists)
least_fav = 'Eminen'
artists.remove(least_fav)
print (artists)
print ("I don't like songs of " + least_fav + '.')

#Exercise
guests = ['stephen', 'laura', 'kekeli', 'Cletus', 'racheal']
message4 = '\nDear ' + guests[0].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[1].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[2].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[3].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
unavailable = '\ncletus'
print (unavailable.title() + ' is unavailable')

guests[3] = 'kelvin'
message4 = '\nDear ' + guests[0].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[1].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[2].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[3].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)

print ( '\nI decided to invite more people since I found a bigger place to host the dinner.')
guests.insert(2, 'princess')
guests.insert(0, 'micheal')
guests.append('stella')
print (guests)

message4 = '\nDear ' + guests[0].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[1].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[2].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[3].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[4].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[5].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[6].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)
message4 = '\nDear ' + guests[7].title() + ', I would like to invite you to dinner at my house this Sunday.'
print (message4)

print ('\nUnfortunately I can only invite three people for the dinner. Sorry for any inconvinience this may have caused.')

sorry1 = guests.pop()
message5 = '\nDear ' + sorry1.title() + ' due to unforseen circumstances I can no longer accommodate a large number of people so I am making it a family dinner. Sorry for any inconvinience this may have caused.'
print (message5)
sorry1 = guests.pop()
message5 = '\nDear ' + sorry1.title() + ' due to unforseen circumstances I can no longer accommodate a large number of people so I am making it a family dinner. Sorry for any inconvinience this may have caused.'
print (message5)
sorry1 = guests.pop()
message5 = '\nDear ' + sorry1.title() + ' due to unforseen circumstances I can no longer accommodate a large number of people so I am making it a family dinner. Sorry for any inconvinience this may have caused.'
print (message5)
sorry1 = guests.pop(0)
message5 = '\nDear ' + sorry1.title() + ' due to unforseen circumstances I can no longer accommodate a large number of people so I am making it a family dinner. Sorry for any inconvinience this may have caused.'
print (message5)
sorry1 = guests.pop(2)
message5 = '\nDear ' + sorry1.title() + ' due to unforseen circumstances I can no longer accommodate a large number of people so I am making it a family dinner. Sorry for any inconvinience this may have caused.'
print (message5)

print (guests)

message6 = '\nDear ' +guests[0].title()+ ', you are still invited to the dinner.'
print (message6)
message6 = '\nDear ' +guests[1].title()+ ', you are still invited to the dinner.'
print (message6)
message6 = '\nDear ' +guests[2].title()+ ', you are still invited to the dinner.'
print (message6)

del guests[2]
print (guests)
del guests[1]
print (guests)
del guests[0]
print (guests)