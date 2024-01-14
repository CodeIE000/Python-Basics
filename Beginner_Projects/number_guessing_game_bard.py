# NUMBER GUESSING GAME BARD VERSION

import random

random_number = random.randint(0, 999)  # Use randint for inclusive range

def get_valid_guess():
    while True:
        try:
            guess = int(input("Guess a number between 0 and 999: "))
            if 0 <= guess <= 999:
                return guess
            else:
                print("Invalid range. Please choose a number between 0 and 999.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

while True:
    guess = get_valid_guess()
    difference = abs(guess - random_number)

    if guess == random_number:
        print("You got it!")
        break
    elif difference <= 4:
        print("You're really close!")
    elif difference <= 9:
        print("Almost there!")
    else:
        print("Too high" if guess > random_number else "Too low")