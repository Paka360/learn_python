# A guessing game for me to play

from random import randint
secret_number = 2

guess = input("Guess a number between 1 and 10: ")
guess = int(guess)
tries = 0


while tries < 3 and guess != secret_number:
    print("Try again")
    guess = int(input("Guess a number between 1 and 10. "))
    tries += 1
        
if guess == secret_number:
    print("You are right!")


