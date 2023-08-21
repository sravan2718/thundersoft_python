# global variable is created in python

# declare global variable
message = 'hello'

def greet():
    # declare local variables
    print('local',message)

greet()
print('global', message)


#using python global and local variable:

a = 1
# uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)

#variable 'a' is redefined as a local
def g():
    a=2
    print('Inside g() : ',a)

#uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ',a)

#global scope

print('global : ', a)
f()
print('global : ' , a)
g()
print('global : ', a)
h()
print('global : ', a)


#global variables and function parameters:

def func(x, y):
    global a
    a = 45
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)
    a,b,x,y = 3,15,3,4
func(9,81)
print (a)

# example:

def x():
    x = 10

x()

def showX():
    print("the value of x is", x)
    showX(
    



