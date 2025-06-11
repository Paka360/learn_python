#Working with lists

#looping through an entire lists
animals = ['lion', 'cat', 'dog', 'zebra', 'snake', 'goat']
for animal in animals:
    print(animal)

countries = ['ghana', 'benin', 'usa', 'uk', 'china']
for country in countries:
    print(country.title() + " is the best country to be born in.")
    print('I love the people and everything else about ' + country.title()+ ".\n")

print("Every country is unique and special")

#Practise Exercise
phones = ['samsung', 'tecno', 'huawei', 'itel', 'iphone']
for phone in phones:
    print(phone.title())
    print(phone.title() + ' phones are the best phones in the world.\n')
print('I do like other phones too as well since I am somewhat of a tech nerd')

pets = ['dog', 'cat', 'bird', 'sheep', 'goat']
for pet in pets:
    print(pet)
for pet in pets:
    print('a ' + pet + ' is a really good pet.\n')
message = 'They are all very popular pets found in homes.'
print ( message)

#Numerical lists
for value in range(1,5):
    print(value)
for value in range(1,6):
    print(value)
 
numbers = list(range(1,6))
print(numbers)

#Using list and range functions to make a list of number sets
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#Statistics with a list of numbers
digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions
cubes = [value**3 for value in range(1,6)]
print(cubes)

#Practise Exercise
for value in range(1,21):
    print(value)
for value in range(1,1001):
    print(value)

thousand = list(range(1,1001))
print(min(thousand))
print(max(thousand))
print(sum(thousand))

for value in range(1,20,2):
    print(value)

for value in range(3,31,3):
    print(value)

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
print(cubes)

cubes = [value**3 for value in range(1,12)]
print(cubes)