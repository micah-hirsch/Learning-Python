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

# Dictionaries

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_conversions["Nov"]) #give value associated with key
print(month_conversions.get("Dec", "Not a valid key")) # Can give a default value

# While loops

i = 1
while i <= 10:
    print(i)
    i = i + 1

print("Done with loop")

# For loops

for letter in "Giraffe Academy":
    print(letter)

for index in range(10):
    print(index)

# Exponent Function

print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))

# 2D Lists and Nested Loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0]) #will print one from number_grid
print(number_grid[2][1]) # printing out 8 from number_grid

## nested for loop

for row in number_grid:
    for column in row:
        print(column)

# Try/Except
## A way to catch invalid inputs/calculations, etc...

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid Input")

# Reading Files

file_name = open("type name of file or path to the file", "r")  # read mode
file_name = open("type name of file or path to the file", "w")  # can change file
file_name = open("type name of file or path to the file", "a")  # apphend info to end of the file
file_name = open("type name of file or path to the file", "r+")  # read and write mode

file_name.close()

print(file_name.readable())  # is the file readable?
print(file_name.read())  # print out contents of a file
print(file_name.readline())  # print out specific line of a file (line by line)
print(file_name.readline()[1])  # print out line at index 1 of a file

# Writing to files

## Appending a file

file_name.write("add something to file")
file_name.write("\nadd something to file")  # new line character

# Modules and pip

# importing functions from other py files

## import name_of_file  this uses all the functions from a file
## print(name_of_file.function()) using function from different file here

### pip is used in terminal

# Classes and Objects

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

#from file import Student #importing class from separate file (usually)

student1 = Student("Jim", "Business", 3.1, False)  # student object

print(student1.name)  # Access attributes of student object

# Object functions

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student2.on_honor_roll())
