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
def get_formatted_name(firstname, lastname,  middlename = ''):
    """Return a fullname, neatly formatted"""
    if middlename:
        fullname =  fullname = firstname+' ' +middlename+ ' ' +lastname
    else:
        fullname = firstname+ ' ' +lastname
    return fullname.title()
musician = get_formatted_name('king', 'promise')
print(musician)
artist = get_formatted_name('celine', 'dion', 'anna')
print(artist)