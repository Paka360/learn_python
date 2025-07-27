#Classes
#Creating and using a class
#Creating the Dog Class
class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over."""
        print(self.name.title() + " rolled over!")

#Making an instance From a Class
my_dog = Dog('max',6)

print("My dog's name is "+ my_dog.name.title() +'.')
print("My dog is "+str(my_dog.age)+ ' years old.')

my_dog.sit()
my_dog.roll_over()

#Creating Multiple Instances
my_dog = Dog('max', 10)
your_dog = Dog('lucy', 7)

print("My dog's name is "+ my_dog.name.title() +'.')
print("My dog is "+str(my_dog.age)+ ' years old.')
my_dog.sit()

print("Your dog's name is "+ your_dog.name.title() +'.')
print("Your dog is "+str(your_dog.age)+ ' years old.')
your_dog.sit()

#Practice Exercise
class Restaurant():
    """Making a model of a restaurant"""

    def __init__(self, name, location):
        """Initializing name and location attributes"""
        self.name = name
        self.location = location
    
    def open(self):
        """Opens the restaurant"""
        print("You are warmly Welcome")

    def closed(self):
        """Closes the restaurant"""
        print("We are closed. Sorry for any inconvenience caused.")

fav_restaurant = Restaurant('Calabash', 'Engineering gate')
print("Mike lets go and buy food at " + fav_restaurant.name.title() + ".")
print("The distance is not far. It is located at " + fav_restaurant.location.title())
fav_restaurant.open()
fav_restaurant.closed()

food_joint = Restaurant('silver lobster', 'republic hall')
bush_canteen = Restaurant('chickenman', 'commercial area')

class User():
    """Making a model of a user"""

    def __init__(self, firstname, lastname):
        """Initializing user name"""
        self.firstname = firstname
        self.lastname = lastname

    def describe_user(self):
        """This describes the user"""
        print("The user is "+ self.firstname.title() +' '+ self.lastname.title()+ "." )
        print("He signed up in March last year.")

    def greet_user(self):
        """This greets the user"""
        print("You are welcome "+self.firstname.title()+' '+ self.lastname.title()+'.')

user_1 = User('Kelvin', 'Danquah')
user_1.describe_user()
user_1.greet_user()

    
