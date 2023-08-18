#python global variable

c = 1 # global variable

def add():
    print(c)

add()


#global variable
c = 1

def add():


    # use of global keyword
    global c

    # increment c by 2
    c = c + 2

    print(c)

add()


#global in nested function:


def outer_function():
    num = 20


    def inner_function():
        global num
        num = 25

    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)
 
outer_function()
print("outside both function:",num)



#Accessing global variable from inside a function:

# global variable
a = 15
b = 10

# function to perform addition
def add():
    c = a + b
    print(c)

#calling a function
add()


#changing a global variable from inside a function using global:

x = 15

def change():
    #using a global keyword
    global x
    #increment value of a by 5
    x = x + 5
    print("value of x inside a function :", x)

change()
print("value of x outside a function :", x)


#modifying list elements without using global keyword:

arr = [10, 20, 30]

def fun():
    for i in range(len(arr)):
        arr[i] += 10

print("'arr' list before excuting fun():", arr)
fun()
print("'arr' list after excuting fun():", arr)

#example:

x=1
def change_global():
   global x
   x = 2
change_global()
print(x)
  
  #global varaible:
  
  #import both config and update module
import config
import update
  #print the update value
print("Modified value of name:"+ config.name)
print("Modified value of year:",config.year)