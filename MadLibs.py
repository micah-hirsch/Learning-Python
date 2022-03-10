# This is a test project creating a Mad Libs game. This is based on the Youtube tutorial by freeCodeCamp.org. Tutorial by Kylie Ying.
# Link to Youtube tutorial: https://youtu.be/8ext9G7xspg

# String Concatenation Intro
youtuber = "" # Some String

# A few ways to do this
print("subscribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

# MadLib Game: Based off of the Youtube tutorial

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)

# Second Madlib Game: My own
place = input("Place: ")
adj = input("Adjective: ")
noun = input("Noun: ")
adj2 = input("Adjective: ")
verb = input("Verb: ")

madlib2 = f"I always wanted to go to {place}. I hear there are very {adj} animals there. One of \
the things they are known for are their famous {noun}. They say its so {adj2} that you can {verb} all day!"

print(madlib2)