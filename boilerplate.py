"""SCRIPT"""

# BOILERPLATE
import random

# this generates a random number between 1 and 10
number = random.randint(1, 10)

TRIES = 0
if TRIES > 3:
    print("you lose")
    

# GAME LOOP
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("correct")
        break
        

    if guess > number:
        print("too high")
        
    else:
        print("Too low")
        break

    # implement your logic below
