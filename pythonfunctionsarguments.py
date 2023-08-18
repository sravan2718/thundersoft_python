#Required arguments:

def add_numbers( a = 7, b = 8):
    sum = a + b
    print('sum:', sum)

#function call with two arguments
add_numbers(2, 3)

#function call with one arguments
add_numbers(a = 2)

#function call with no arguments
add_numbers()


#example

def display_info(first_name, last_name):
    print('First Name:' , first_name)
    print('Last Name:' ,last_name)


display_info(last_name = 'anil' , first_name = 'rutthala')

# example:

def display (a, b):
print (a, b)
display(a = 10, b = 20)



#keyword arguments:

def my_function(child3, child2, child1):
    print("the youngest child is " + child3)

my_function(child1 = "prasad", child2 = "prem", child3 = "john")


#example:

#function defintion is here
def printinfo( name, age ):
    print("Age", age)
    return;
#now you can call printinfo function
printinfo (age=50, name="mikki")

#example:

def display (a, b):
    print(a, b)

display(b = 20, a = 10)

#Default arguments:

def student(firstname, lastname='Mark', standard='Fifth'):
     print(firstname, lastname, 'studies in',standard, 'standard')
     
# 1 positional arguments
student('john')

# 3 positional arguments
student('john', 'gates', 'seventh')

# 2 positional arguments
student('john', 'gates')
student('john', 'seventh')


#mutable default argument values example using python list:

#itemname is the name of the item that we want to add to list that is being passed,or if it is not passed then appending in the default list

def appendItem(itemname, itemlist = []):
     itemlist.append(itemname)
     return itemlist
     
print(appendItem('notrbook'))
print(appendItemtime('pencil'))
print(appendItem('eraser'))

#example:

def display(name,course="btech"):
        print(name)
        print(Course)
display (name = "abc", course="Mtech")
display (name = "pqr")


#variable length arguments:

#begining of the method
def sum(*args):
    resultfinal = 0
#begining of for loop
    for arg in args:
       resultfinal = resultfinal + arg
       
     return resultfinal
#printing the values
print(sum(10, 20))
print(sum(10, 20, 30))
print(sum(10, 20, 2))

#finding the multiplication:

def multiplier(*num):
    prod = 1
#initialize prod variable with zero
    for i in num:
        prod = prod * i
        
    print("product:",prod)
    
multiplier(3,5)
multiplier(1,2,4)
multiplier(2,2,6,7)

#example:

def display (* courses ):
    for i in courses:
       print(i)
display("Btech", "Mtech", "Mca", "Mba")






