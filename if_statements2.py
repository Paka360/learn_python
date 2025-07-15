#Using if staements with lists
cooking_rice = ['oil', 'rice', 'water', 'salt']
for cooking_ric in cooking_rice:
    print ("Add " + cooking_ric + '.')
print ("leave to boil.Your rice is ready!.\n")

cooking_rice = ['oil', 'rice', 'water', 'salt']
for cooking_ric in cooking_rice:
    if cooking_ric == 'salt':
        print ("There is no salt. we need to buy some.")
    else:
        print ("Add "+ cooking_ric + '.')
print ("leave to boil.Your rice is ready!.")

#checking that a list is not empty

toys = []
if toys:
    for toy in toys:
        print ('Buy me a ' + toy + '.')
    print("Here you are.")
else:
    print("\nThe toy shop is closed.\n")
    toys = ['car', 'motorbike', 'doll']
if toys:
    for toy in toys:
        print ('Please buy me a ' + toy + '.')
    print("Here you are!\n")
else:
    print("\nThe toy shop is closed.")

#Using multiple lists
available_toppings =['mushrooms', 'olives', 'green pepper', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings =['mushrooms', 'frenchfries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print ("Adding " + requested_topping+ '.')
    else:
        print("Sorry we don't have "+ requested_topping+ '.')
print ("Finished making your pizza!\n")

#Practise Exercise
users = ['john', 'eric', 'mike', 'joe', 'elsie', 'sarah', 'ella', 'admin']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report.\n")
    else:
        print ("Hello "+ user.title()+ ", thank you for logging in again.\n")
    
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report.\n")
        else:
            print ("Hello "+ user.title()+ ", thank you for logging in again.\n")
else:
    print('We need to get people to sign up!')

del users[0:8]
print(users)
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report.\n")
        else:
            print ("Hello "+ user.title()+ ", thank you for logging in again.\n")
else:
    print('We need to get people to sign up!\n')

current_users = ['eric', 'sarah', 'laura', 'moses', 'mike']
new_users = ['kekeli', 'eric', 'stella', 'Moses', 'hannah']

for new_user in new_users:
    new_user = new_user.lower()
    if new_user in current_users:
        print (new_user.lower() +". This username is not available. Please try a new username.\n")
    else:
        print (new_user.lower() + ". This username is available.\n")

positions = [1,2,3,4,5,6,7,8,9]
for position in positions:
    if position == 1:
        print(str(position) + 'st')
    elif position == 2:
        print(str(position) + 'nd')
    elif position == 3:
        print(str(position) + 'rd')
    else:
        print(str(position) + 'th')


