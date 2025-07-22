#Defining a function
def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()

#Passing Information to a function
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " +username.title() +"!")

greet_user('jesse')
greet_user('sarah')

#Passing Arguments
#Positional Arguments
# def describe_pets(animal_type, pet_name):
#     """Display information about a pet."""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() +".")

# describe_pets('dog', 'max')
# describe_pets('cat', 'gutus')
# describe_pets('mouse', 'jerry')

# def call_mom():
#     """Displaying Information about my mother"""
#     message = input("Where is your mother? ")
#     print(message)
#     print("This is my number. Tell her to call me when she returns. She should be back any moment from now.")

# call_mom()

#Keyword Arguments
def describe_pets(animal_type, pet_name):
    """Displaying information abouy a pet"""
    print("\nI have a "+ animal_type +'.')
    print("My "+ animal_type + "'s name is "+pet_name.title() +".")

describe_pets(animal_type = 'hamster', pet_name = 'max')

#Default Values
def describe_pets( pet_name, animal_type = 'dog'):
    """Displaying information abouy a pet"""
    print("\nI have a "+ animal_type +'.')
    print("My "+ animal_type + "'s name is "+pet_name.title() +".")

describe_pets(pet_name = 'max')

#When a value is provided the default value is ignored
def describe_pets( pet_name, animal_type = 'dog'):
    """Displaying information abouy a pet"""
    print("\nI have a "+ animal_type +'.')
    print("My "+ animal_type + "'s name is "+pet_name.title() +".")

describe_pets(pet_name = 'max', animal_type = 'fish')

#Practice Exercises
def make_shirt(size, message):
    print("\nOrder ready for  "+ size + " size shirt with " + message + " printed at the back.")

make_shirt('small', 'Messi')

def make_shirt(size, message):
    print("\nOrder ready for "+ size + " size shirt with " + message + " printed at the back.")

make_shirt(size = 'large', message = "Courtios")

def make_shirt(message, size = 'large'):
    print("\nOrder ready for "+ size + " size shirt with " + message + " printed at the back.")

make_shirt(message = "Bellingham")

def places(city, country):
    print('\n' + city.title() + " is in " + country.title() +'.')

places('accra', 'ghana')
places('london', 'uk')

def places(city, country = 'ghana'):
    print('\n' + city.title() + " is in " + country.title() +'.')

places('accra', 'ghana')
places('kumasi')
places('texas', 'usa')

#Values
#Returning simple values
def get_formatted_name(firstname, lastname):
    """Return a fullname, neatly formatted"""
    fullname = firstname+' ' +lastname
    return fullname.title()
musician = get_formatted_name('king', 'promise')
print(musician)

#Making an argument optional
# def get_formatted_name(firstname, lastname,  middlename = ''):
#     """Return a fullname, neatly formatted"""
#     if middlename:
#         fullname =  fullname = firstname+' ' +middlename+ ' ' +lastname
#     else:
#         fullname = firstname+ ' ' +lastname
#     return fullname.title()
# musician = get_formatted_name('king', 'promise')
# print(musician)
# artist = get_formatted_name('celine', 'dion', 'anna')
# print(artist)

# #Returning a dictionary
# def build_person(firstname, lastname, age =""):
#     """Return a dictionary of information about a person"""
#     person = {'first': firstname, 'last':lastname}
#     return person

# actor = build_person('tom', 'cruise')
# print(actor)

# def build_person(firstname, lastname, age =""):
#     """Return a dictionary of information about a person"""
#     person = {'first': firstname, 'last':lastname}
#     if age:
#         person['age'] = age
#     return person

# actor = build_person('tom', 'cruise', age = 52)
# print(actor)

# #Using a function with a while loop
# # def get_formatted_name(firstname, lastname):
# #     """Return a full name neatly formatted"""
# #     fullname = firstname + ' '+ lastname
# #     return fullname.title()

# # while True:
# #     print("\nPlease enter your name: ")
# #     print("(Enter quit when you are done)")

# #     f_name = input("First name: ")
# #     if f_name =="quit":
# #         break

# #     l_name = input("\nLast name: ")
# #     if l_name == "quit":
# #         break

# #     formatted_name = get_formatted_name(f_name, l_name)
# #     print("\nHello, " + formatted_name +"!") 

# #Practice Exercise
# def capital_towns(country, capital):
#     country = country + ", " + capital
#     return country.title()

# ghana = capital_towns('ghana', 'accra')
# print(ghana)
# china = capital_towns('china', 'hong kong')
# print(china)
# russia = capital_towns('russia', 'moscow')
# print(russia)

# def build_album(artist, title):
#     """Describing an album"""
#     album = {'art':artist, 'tit':title}
#     return album

# album_1 = build_album('ed sheeran', 'divide') 
# print(album_1)

# def build_album(artist, title, tracks=""):
#     """Describing an album"""
#     album = {'art':artist, 'tit':title}
#     if tracks:
#         album['tracks'] = tracks
#     return album

# album_1 = build_album('ed sheeran', 'divide', '12') 
# print(album_1)

# def build_album(artist, title, tracks=""):
#     """Describing an album"""
#     album = {'art':artist, 'tit':title}
#     return album
# while True:
#     print("\nEnter the album information: ")
#     print("(Please enter 'quit' when you are done)")
    
#     musician = input("What is the name of the artist: ")
#     if musician == 'quit':
#         break

#     title1 = input("What is the title of the album: ")
#     if title1 == 'quit':
#         break

#     album_1 = build_album(musician, title1,) 
#     print(album_1)

#Passing a list
def greet_users(names):
    """Print a simple message to each user in the lost"""
    for name in names:
        message = "Hello, "+ name.title() + '!'
        print(message)

usernames = ['hannah', 'tyland', 'john']
greet_users(usernames)

#Modifying a list in a function
unprinted_designs = ['iphone case', 'robot pendant', 'slippers', 'dog chain']
completed_models = []

#simulate printing each design
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #simulate printing a 3D print from each design
    print("Printing model: "+ current_design)
    #moving each design to completed_models after printing
    completed_models.append(current_design)

#Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

def print_models(unprinted_designs, completed_models):
    """simulate printing each design until none is left. Move each design to completed_models after printing"""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: "+ current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'dog chain', 'pendant', 'slippers']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


def introduce_magicians(magicians):
    for magician in magicians:
        print("\nLadies and gentlemen, please welcome "+ magician +' with a round of applause.')

magicians = ['berkley', 'harry potter', 'dumbledore', 'slyterin', 'haffelpop']
introduce_magicians(magicians)

def great_magicians(magicians):
    for magician in magicians:
        print('\nThe Great '+ magician.title() + '!' )

magicians = ['berkley', 'harry potter', 'dumbledore', 'slyterin', 'haffelpop']
great_magicians(magicians)