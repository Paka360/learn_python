#User input
message = input("Tell me something and I will repeat it back to you: ")
print(message)
name = input("Please enter your name: ")
print("Hello, "+ name + "!")

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