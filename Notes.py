# This script is practice code and notes based on a beginner Python tutorial.
# "Learn Python - Full Course for Beginners" from freeCodeCamp.org
# Instructed by Mike Dane
# Link: https://youtu.be/rfscVS0vtbw

# Variables and Data Types

#importing python math

from math import *

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

print(2) # Just printing the number integer
print(2.09) # float
print(3 + 4.5) # addition, but also subtraction, multiplication, division, ... etc.
print(10 % 3) # modulus operator gives you the remainder from 10/3
my_num = 5
print(my_num) # storing number variable then printing it out
print(str(my_num)) #converting into a string

## Functions (Not an exhaustive list)
print(abs(my_num)) # absolute value of the number
print(pow(10, 3)) # 10 ^ 3 "to the power"
print(max(10, 3)) # return the largest number
print(min(10, 3)) # print out the smallest number
print(round(3.2)) # rounding a number according to typical rounding rules
print(floor(3.7)) # getting the lowest number
print(ceil(3.2)) # rounding number up (i.e. 4)
print(sqrt(36)) # square root function

# Getting Input from Users

name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hi {name}! You are {age} years old.")

# Lists

friends = ["Austin", "Rowan", "Cassie"]
print(friends)
print(friends[1]) # Getting item in second position of the list
print(friends[-1]) # starts from the back of the list
print(friends[1:]) # indexing a range of names
print(friends[0:1])
friends[2] = "Stephanie" # modifying values in list. This will replace "Cassie" with "Stephanie"

# List Functions

lucky_numbers = [4, 8, 15, 16, 25, 30]
friends.extend(lucky_numbers) # appending lucky numbers list on the friends list
friends.append("Caitlin")# Adding an additional item to end of list
friends.insert(1, "Alyssa") # Adding an additional item at index position 1 (second item)
friends.remove("Austin") #removing Austin from the freinds list
friends.clear() #empties the list
friends.pop() # gets rid of the last element in the list
print(friends.index("Rowan")) # is Rowan in the list?
print(friends.count("Austin")) # count number of times an element appears in the list
friends.sort() # sort list in ascending order
lucky_numbers.sort() # ascending order
lucky_numbers.reverse() # reverse the order of the list
friends2 = friends.copy() # copying a list

# Tuples

coordinates = (4, 5) #tuple with coordinates

## Tubles are immutable. They cannot be changed or modified once created.

print(coordinates[1]) # index

list_coordinates = [(4, 5), (6, 7), (8, 9)] # a list of tuples

# Functions

def say_hi():
    print("Hello User")

say_hi()

def say_hi(name):
    print(f"Hello {name}")

say_hi("Micki")

# Return Statement

def cube(num):
    return num*num*num

result = cube(4)
print(result)

# If Statements

is_male = False
is_tall = False

if is_male or is_tall:
    print("You are either male,tall, or both")
else:
    print("You are neither male or tall")

if is_male and is_tall:
    print("You are male and tall")
else:
    print("You are either not male, not tall, or both")

if is_male and is_tall:
    print("You are male and tall")
elif is_male and not(is_tall):
    print("You are a male, but not tall")
elif not(is_male) and is_tall:
    print("You are not a male, but you are tall")
else:
    print("You not a male and not tall")

# If statements & comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

