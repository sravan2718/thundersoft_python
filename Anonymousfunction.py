#lambda function example:

str1 = 'GeeksforGeeks'

upper = lambda string: string.upper()
print(upper(str1))


#number is passed as a parameter to perform operations

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", format_numeric(1000000))
print("float formattimg:",format_numeric(999999.78951235))


#diff b|w lambda function and def defined function:

def cube(y):
    return y*y*y
lambda_cube = lambda y: y*y*y

# using function defined
print("using function defined with 'def' keyword, cube:", cube(5))

# using the lambda function
print("using lambda function, cube:", lambda_cube(5))


#python lambda function with list comprehension:

is_even_list = [lambda arg=x: arg* 10 for x in range(1, 5)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())

#python lambda with multiple statement:

List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# sort each sublist
sortlist = lambda x: (sorted(i) for i in x)

#get the second largest element
secondlargest = lambda x, f :[y[len(y)-2] for y in f(x)]
res = secondlargest(List, sortlist)
print(res)

#filter out all odd numbers using filter()and lambda function

l2 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), l2))
print(final_list)


#transform all elements of a list to upper case using lambda and map()

#use of lambda() function
#with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

#to upper case and return the same
uppered_animals = list(map(lambda animal: animal.upper(), animals))

print(uppered_animals)

# sum of all elements in a list using lambda and reduce()function

# reduce() with lambda()
# to get sum of a list

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)


#find the maximum element in a list using lambda and reduce()function

#with a lambda function

#importing functools for reduce()
import functools

#initializing list
lis = [1, 3, 5, 6, 2 ]

#using reduce to compute maximum element from list
print("the maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))


#Example :


def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))




