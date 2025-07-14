'''#Introduction to while loops
current_number = 1
while current_number < 6:
    print(current_number)
    current_number += 1


prompt = "\nTell me something nice, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program: "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

#using flags
running = True
while running:
    message = input(prompt)
    if message == 'quit':
        running = False
    else:
        print(message)   

#Using break to exit a loop
prompt = "\nPlease enter the name of your favourite countries: "
prompt += "\nEnter 'quit' when done. "

while True:
    city = input(prompt)
    if city =='quit':
        break
    else:
        print("I like " + city.title() +'!' )

#Using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#Practice exercise
prompt = "\nEnter the toppings you would like for your pizza please."
prompt += "Enter 'quit' after you are done."

order = ""
while order != 'quit':
    order = input(prompt)
    if order != 'quit':
        print(order.title() + " wil be added to your pizza. Thank you for patronizing!") '''

''' prompt = "\nHow old are you?"
age = ''
flag = True
while  flag == True:
    age = input(prompt)
    age = int(age)
    if age <= 3:
        print("You are free to enter.")
        flag = False
    elif age <= 12:
        print("Your ticket will cost $10.")
        flag = False
    elif age > 12:
        print("Your ticket will cost $15.") 
        flag = False 

#Using While loops with lists and dictionaries
#Moving items from one list to another

unconfirmed_users = ['alice', 'mike', 'hannah', 'jane']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " +current_user.title() )
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title()) '''

#Removinig all istances of a specific value from a list
pets = ['cat', 'dog', 'cat', 'pig', 'mouse', 'bird', 'cat', ]
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

'''
#User input
message = input("Tell me something and I will repeat it back to you: ")
print(message)
name = input("Please enter your name: ")
print("Hello there, "+ name + "!")

prompt = "If you tell us who youare we can personalize your messages."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("Hello, "+ name+ '!')

age = input("How old are you? ")
age = int(age)
print(age)
if age>= 40:
    print("You are old!")

height = input("How tall are you in inches? ")
height = int(height)

if height >= 36:
    print('\nYou are tall enough to ride.')
else:
    print('\nYou are too short to ride.')

number = input("Enter a number and I'll tell you if it is even or odd: ")
number = int(number)

ans = number % 2
if ans == 0:
    print("The number " +str(number) +" is even.")
else:
    print("The number " +str(number) +" is odd.")

#practice exercise
message = input("Which car would you like to rent? ")
print("let me see if we have a "+ message + " available")

people = input("How many people are you expecting? ")
people = int(people)
if people >= 6:
    print("We do not have a table to accomodate such a large group. ")
else:
    print("Please come right this way.")

number = input("Enter a number and I'll tell you if it is a multiple of 10: ")
number = int(number)

ans = number % 10
if ans == 0:
    print("The number " +str(number) +" is a multiple of 10.")
else:
    print("The number " +str(number) +" is not a multiple of 10.")

message = input("What is your favourite song? ")
print(message)
'''
'''#filling dictionaries with user input
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input('\nWho would you like to vote for? ')
    responses[name] = response
    
    repeat = input('\nPlease are you done voting? (yes/no)')
    if repeat == 'yes':
        polling_active = False

print("\n   Poll Results    ")
for name, response in responses.items():
    print(name + " voted for "+ response +".")'''
   
#Practice Exercise
'''food_orders = ['banku', 'rice', 'jollof', 'waakye', 'sandwich', 'pizza', 'porridge', 'turkey']
finished_orders = []
still_preparing = True
while still_preparing:
    current_dish = food_orders.pop()
    print("\nI am currently preparing " + current_dish +'.')
    print('\nI am all done. What is the next dish?')
    finished_orders.append(current_dish)
    if food_orders == []:
        still_preparing = False
print('\n All the orders are ready, if you hera your dish come for it.')
for order in finished_orders:
    print(order)'''

submissions = {}
polls_active = True
while polls_active:
    name = input('\nWhat is your name? ')
    places = input('\nIf you could visit one place in the world where would it be? ')
    submissions[name] = places

    repeat = input('\nIs that the only place? (yes/no).')
    if repeat == 'yes':
        polls_active = False
print('\n    Poll Results    ')
for name, place in submissions.items():
    print(name.title() + ' would like to visit ' + place.title() +'.')