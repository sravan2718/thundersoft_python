#example with single dimension:

import array
# 0 1 2 3
A=array.array('i',[10,20,30,40])
print(A)
print(type(A))
A=array.array('f',[12.3,45.6,78.9,45.2])
print(A)
print(type(A))

from array import *
A=array('i',[10,20,30,40])
print(A)
print(type(A))
print(A.typecode)
print(A[2])
A.insert(1,34)
print(A)
A.append(45)
print(A)
A.extend([67,89,90])
print(A)
A.remove(30)
print(A)
A.reverse()
print(A)


#To display array element for using loop:

from array import *
A=array('i',[100,200,300,400,500,600])
for i in A:
 print(i)
 
for i in range(len(A)):
 print(A[i])


#Copying elements from one array to another:
 
from array import *
A=array('i',[2,3,4,5,6])
print(A)
#B=A
#print(B)
B=array(A.typecode,[i*2 for i in A])
print(B)

#creating array by accepting elements at run time#

from array import *
A=array('i',[])
n=int(input("Enter length of the array:"))
for i in range(n):
 x=int(input("Enter value:"))
 A.append(x)
print(A)


#numpy methods:

#Example with numpy arrays

import numpy
#A=numpy.array([10,20,30,40,50])
A=numpy.array([10,20,30,40,50.8],int)
print(A)
print(type(A))
print(A.dtype)
print(A.ndim)
print(A.size)
print(A.shape)

#Example2:

from numpy import *
A=linspace(2,20,7)#start,stop,no of parts
print(A)
A=logspace(3,15,6)
print(A)
A=arange(2,20,3)#start,stop,step
print(A)
A=zeros(6,int)
print(A)
A=ones(6,int)
print(A)



