 #my module example:

def greeting(name):
    print("Hello, " + name)
    
#import the module and call the greeting function

import mymodule
mymodule.greeting("jonathan")


#variable in module:

person1 = {
    "name": "john",
    "age" : 36,
    "country" : "india"
}

#person1dictionary

import mymodule

a = mymodule.person1["age"]
print(a)

#import specific attributes from a python module:

# importing sqrt () and factorial from the module math
from math import sqrt,factorial

# if we simply do "import math", then
#math.sqrt(16) and math.factorial() are required.
print(sqrt(16))
print(factorial(6))

#python built in modules:

# importing built-in module math
import math

# using square root(sqrt) function contained in math module
print(math.sqrt(25))

#using pi function contained in math module
print(math.pi)

# 2 radians = 114.59 degrees
print(math.degrees(2))

#60 degrees = 1.04 radians
print(math.radians(60))

#sine of 2 radians
print(math.sin(2))

#cosine of 0.5 radians
print(math.cos(0.5))

#tangent of 0.23 radians
print(math.tan(0.23))

# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))

#importing built in module random
import random

#printing random integer between 0 and 5
print(random.randint(0, 5))

#print random floating point number between 0 an 1
print(random.random())

#random number between 0 and 100
print(random.random() * 100)

list = [1, 4, True, 800, "pythom", 27, "hello"]

#using choice function in random module for choosing a random element from a set such as a list
print(random.choice(list))

#importing built in module datetime
import datetime
from datetime import date
import time

#returns the number of seconds since the unix epoch, january 1st 1970
print(time.time())

#converts a number of second to a date object
print(date.fromtimestamp(454554))


