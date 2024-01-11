# NUMBER GUESSING GAME

import random
import sys

random_number = random.randrange(0, 999)
print("GUESS THE NUMBER 0 - 999")

def getNumber():
    guessed_number = int(input("=> "))

    if guessed_number > 999 or guessed_number < 0:
        print("Choose number only from 0 - 999!")
        return getNumber()
    
    else:
        return guessed_number

def checkNumber():
    guessed_number = getNumber()
    if guessed_number == random_number:
        print("You got it!")
        sys.exit()
    elif guessed_number > random_number:
        if guessed_number - random_number >= 1 and guessed_number - random_number < 5:
            print("You're really close, a bit lower!")
            return checkNumber()
        elif guessed_number - random_number >= 5 and guessed_number - random_number < 10:
            print("Almost There, decrease it!")
            return checkNumber()
        elif guessed_number - random_number > 10:
            print("Too High!")
            return checkNumber()
    else:
        if random_number - guessed_number >= 1 and random_number - guessed_number < 5:
            print("You're really close, a bit higher!")
            return checkNumber()
        elif random_number - guessed_number >= 5 and random_number - guessed_number < 10:
            print("Almost There, increase it!")
            return checkNumber()
        elif random_number - guessed_number > 10:
            print("Too Low!")
            return checkNumber()


checkNumber()
