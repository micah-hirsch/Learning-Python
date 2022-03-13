# This script is practice code and notes based on a beginner Python tutorial.
# "Learn Python - Full Course for Beginners" from freeCodeCamp.org
# Instructed by Mike Dane
# Link: https://youtu.be/rfscVS0vtbw

# Variables and Data Types

## Strings

character_name = "George" # Just change variable to change story below
character_age = "70"

### Can use f strings or + variable. Either way works.
print("There once was a man named" + character_name + ", ")
print(f"he was {character_age} years old. ")
print(f"He really liked the name {character_name}, ")
print("but didn't like being " + character_age + ".")

## Numbers

character_age = 50 # integer
character_age = 50.5 # float

## Booleans

is_male = True

# Working with strings

phrase = "Motor Speech Disorders"

print("Motor Speech Disorders")
print("Motor Speech \n Disorders") # adds a line
print("Motor \"Speech\" Disorders") # how to add quotation marks
print(phrase)
print(phrase + "are speech disorders.")
print(f"{phrase} are speech disorders")

## Functions (Not exhaustive)
print(phrase.lower()) # Lower case
print(phrase.upper()) # Upper case
print(phrase.isupper()) # checking to see if string is upper case
print(phrase.upper().isupper()) # changing to upper case then checking if it is upper case
print(len(phrase)) # length function
print(phrase[0]) # finding first character of string
print(phrase.index("o")) # index function. Passing a parameter. finding position of first "o"
print(phrase.replace("Disorders", "Conditions")) # replace function

# Working with numbers
