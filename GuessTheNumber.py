# Guess the number coding tutorial from freeCodeCamp.org instucted by Kylie Ying.
# Youtube link: https://youtu.be/8ext9G7xspg

import random

# Guess the number chosen by the computer

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Yay! Congrats! You have guessed the number {random_number} correctly")
guess(10)

# Computer guesses our number

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} to high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay! The computer guessed {guess} correctly!")

computer_guess(10)
