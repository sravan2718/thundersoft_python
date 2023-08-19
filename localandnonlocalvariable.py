#local variable:


def sum(x,y):
    
  sum = x + y
  return sum

print(sum(5, 10))


#creating loacal variable in python:


def f():
    # local  variable
    s = " I love cricket"
    print(s)

# driver code
f()


#creating a global variable in python:


#this function uses global variables
def f():
    print("Inside function", s)

# Global scope
s = " I love biryani"
f()
print("Outside a function", s)


#example:

# This function has a variable with
#name same as s.
def f():
    s = "Me too."
    print(s)

#Global scope
s = "I love cricket"
f()
print(s)


#N0N LOCAL KEYWORD:

def foo():
    name = "geek" # local variable

    def bar():
        nonlocal name
        name = 'geeksforgeek'
        print(name)

    # calling inner function
    bar()

    #printing local variable
    print(name)

foo()


#non local varible:


def foo():
    name = "geek"
    def bar():
        name = "Geek"
        # second inner function
        def ack():
             nonlocal name
             print(name)
             name = 'GEEK'
             print(name)
        ack() # calling second inner function

    bar() # calling  first inner function
    print(name) # pinting local variable of bar()

foo()


#non local variable:

def outer_function():
    x = 10

def inner_function():
    nonlocal x
    x = 5
    print("Inside the function, x is:",x)

    inner_function()
    print("outside the function, x is:", x)
    outer_function()


















