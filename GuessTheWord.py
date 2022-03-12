# Guess the word (i.e.Hangman) Game: Based on the 12 Beginner R Projects Youtube Tutorial by freeCodeCamp.org
# Instructed by Kylie Ying
# Link to Youtube Tutorial: https://youtu.be/8ext9G7xspg

import random
from words import words # Calling on the words object in words.py
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def word_guess():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #letters user guessed

    lives = 8

    while len(word_letters) > 0 and lives > 0: # len() is length
        # letters used
        print("You have", lives, "lives left. You have used these letters: ", " ".join(used_letters))

        #what current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not in the word. Try again.")

        elif user_letter in used_letters:
            print("You have already used that letter. Please guess again.")

        else:
            print("Invalid character. Please try again.")
    if lives == 0:
        print("You lost. The word was ", word)
    else:
        print("You guessed the word", word, "!!")

word_guess()
