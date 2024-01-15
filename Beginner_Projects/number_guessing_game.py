# NUMBER GUESSING GAME

import random
import sys

random_number = random.randrange(0, 999)
print("GUESS THE NUMBER 0 - 999")

def get_number():
    guessed_number = int(input("=> "))

    if guessed_number > 999 or guessed_number < 0:
        print("Choose number only from 0 - 999!")
        return get_number()
    
    else:
        return guessed_number

def check_number():
    guessed_number = get_number()
    if guessed_number == random_number:
        print("You got it!")
        sys.exit()
    elif guessed_number > random_number:
        if guessed_number - random_number >= 1 and guessed_number - random_number < 5:
            print("You're really close, a bit lower!")
            return check_number()
        elif guessed_number - random_number >= 5 and guessed_number - random_number < 10:
            print("Almost There, decrease it!")
            return check_number()
        elif guessed_number - random_number > 10:
            print("Too High!")
            return check_number()
    else:
        if random_number - guessed_number >= 1 and random_number - guessed_number < 5:
            print("You're really close, a bit higher!")
            return check_number()
        elif random_number - guessed_number >= 5 and random_number - guessed_number < 10:
            print("Almost There, increase it!")
            return check_number()
        elif random_number - guessed_number > 10:
            print("Too Low!")
            return check_number()


check_number()


