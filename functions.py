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
def describe_pets(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() +".")

describe_pets('dog', 'max')
describe_pets('cat', 'gutus')
describe_pets('mouse', 'jerry')