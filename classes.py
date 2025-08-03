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

#Working with Classes and Instances
class Car():
    """A simple attept to model a car"""

    def __init__(self, make, model, year):
        """Initializes attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted name"""
        long_name = str(self.year)+ ' ' +self.make+ ' ' + self.model
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#Setting a default value for an attribute
class Car():

    def __init__(self, make, model, year):
        """Initializing attributes to describe a car"""
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
         """Return a neatly formatted name"""
         long_name = str(self.year)+ ' ' +self.make+ ' ' + self.model
         return long_name.title()       

    def read_odometer(self):   
        """Print a statement showing the car's mileage."""
        print("This car has " +str(self.odometer_reading)+ " miles on it.") 
    
my_car = Car('audi', 'a5', '2018')
print(my_car.get_descriptive_name())
my_car.read_odometer()
        

#Modifying Attribute Values
my_car.odometer_reading = 23
my_car.read_odometer()

#Using Method's to modify an attribute
class Car():

    def __init__(self, make, model, year):
        """Initializing attributes to describe a car"""
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
         """Return a neatly formatted name"""
         long_name = str(self.year)+ ' ' +self.make+ ' ' + self.model
         return long_name.title()       

    def read_odometer(self):   
        """Print a statement showing the car's mileage."""
        print("This car has " +str(self.odometer_reading)+ " miles on it.")

    def update_odometer(self, mileage):
        """Setting odometer value to new value"""
        self.odometer_reading = mileage

car = Car('hondai', 'corolla', 2018)
car.update_odometer(20)
car.read_odometer()

class Car():

    def __init__(self, make, model, year):
        """Initializing attributes to describe a car"""
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
         """Return a neatly formatted name"""
         long_name = str(self.year)+ ' ' +self.make+ ' ' + self.model
         return long_name.title()       

    def read_odometer(self):   
        """Print a statement showing the car's mileage."""
        print("This car has " +str(self.odometer_reading)+ " miles on it.")

    def update_odometer(self, mileage):
        """Setting odometer value to new value
        reject the change if it attempts to roll the odometer back"""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll the odometer back!")

our_car = Car('mercedces', 'corolla', 2020)
our_car.update_odometer(-4)
our_car.read_odometer()

#Practice Exercise
class Restaurant():

    def __init__(self, name, dish, location):
        """Initializing the Attributes"""
        self.name = name
        self.dish = dish
        self.location = location

    def open_restaurant(self):
        """Opens the restaurant"""
        print("We are open.")
    
    def describe_restaurant(self):
        """Describes the restaurant"""
        print("The name of the restaurant is "+ self.name + ". It is locaated at " 
              + self.location + ". Their special dish is " + self.dish )
        
    def close_restaurant(self):
        """Opens the restaurant"""
        print("We are closed.")

fav_restaurant = Restaurant('Sharwama Boiz', 'Sharwama', 'Engineering gate')
fav_restaurant.open_restaurant()
fav_restaurant.close_restaurant()
fav_restaurant.describe_restaurant()


#Inheritance
#The _int_()Method for a Child Class
class Car():
    """A simple attepmt to represent a car"""

    def __init__(self, make, model, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Describe the car"""
        longname = str(self.year) + ' ' + self.make + ' ' +self.model
        return longname.title()
    
    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of car, specific to electric vehicles."""

    def __init__(self, make , model , year):
        """Initialize atributes of the parent class."""
        super().__init__(make, model, year)
    
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# The above section tests the working of the child class to make sure it behaves just like the parent class

#Defining Attributes and Methods for the Child Class
class Car():
    """A simple attepmt to represent a car"""

    def __init__(self, make, model, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Describe the car"""
        longname = str(self.year) + ' ' + self.make + ' ' +self.model
        return longname.title()
    
    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of car, specific to electric vehicles."""

    def __init__(self, make , model , year):
        """Initialize atributes of the parent class.
          After initialize attributes Specific to electric vehicles"""

        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('telsa', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#Instances as Attributes
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size = 70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """Represent aspects of car, specific to electric vehicles."""

    def __init__(self, make , model , year):
        """Initialize atributes of the parent class.
          After initialize attributes Specific to electric vehicles"""

        super().__init__(make, model, year)
        self.battery_size = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())
#my_tesla.battery.describe_battery()
print('Small drops of water make a mighty ocean')


    
        