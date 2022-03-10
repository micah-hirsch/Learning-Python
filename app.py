print("Hello World")
# Intro to Python
age = 20
price = 19.95
first_name = "Mickey"
is_online = False

# Exercise 1
first_name = "John"
last_name = "Smith"
age = 20
is_new = True

# Receive input
name = input("What is your name? ")
print("Hello " + name)

# Type Conversion

birth_year = input("Enter your birth year: ")
age = 2022 - int(birth_year)
print(age)

#float()
#bool()
#str()

# Exercise 2
first = input("Enter first number: ")
second = input("Enter second number: ")
sum = float(first) + float(second)
print("Sum: " + str(sum))

# Strings
course = "Python for Beginners"
print(course.upper())
print(course)
print(course.find("y"))
print(course.replace("for","4"))
print("Python" in course)

# Arithmetic Operations
print(10/3) #division with float as value
print(10//3) #division with integer as value
print(10%3) #remainder
print(10**3) #exponent
x = 10
x = x + 3
x += 3

# Operator Precedence
x = (10 + 3) * 2
x = 10 + 3 * 2

# Comparison Operators
x = 3 > 2 #produces a boolean value
x = 3 == 2 #equality operator
#>
#>=
#<
#<=
#==
#!=

# Logical Operators
price = 25
print(price > 10 and price < 30)
#or
#price(not price > 10)

# if statements
temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature >10:
    print("It's a bit cold")
else:
    print("It's cold")

print("Done")

#Exercise 3
weight = input("Weight: ")
unit = input("kg or lbs: ")

if unit.upper() == "k":
    weight_in_lbs = float(weight) * 2.205
    print("Weight in lbs:" + str(weight_in_lbs))
elif unit.upper() == "l":
    weight_in_kg = float(weight) / 2.205
    print("Weight in kg:" + str(weight_in_kg))

# While Loops
i = 1
while i <= 10:
    print(i * "*")
    i = i + 1

# Lists
names = ["John", "Bob", "Mickey", "Sam", "Mary"]
names[0] = "Jon"
print(names[0:3])

# List Methods
numbers = [1,2,3,4,5]
numbers.append(6)
numbers.insert(0, -1)
numbers.remove(3)
print(numbers)
print(1 in numbers)
print(len(numbers))

# for loops
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

# range function
numbers = range(5, 10, 2)
for number in numbers:
    print(number)

# Tubles
numbers = (1, 2, 3)

