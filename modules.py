
#test.py:

import sample as sm
print(sm.x)
sm.add(10,20) 
sm.mul(30,20)

from sample import x,add,mul
print(x)
add(10,20)
mul(20,30)

from sample import *
print(x)
add(10,20)
mul(20,30)

from sample import x as a,add as sum
print(a)
sum(10,20)


#example importing with multiple modules:

#test.py

from sample import *
from sample1 import *
print(x)
add(2,3)
mul(3,6)
print(x)
sub(7,3)


from sample import *
print(x)
add(2,3)
mul(3,6)
from sample1 import *
print(x)
sub(7,3)


#working with predefined modules:

#working with math module:

from math import *

print(factorial(3))
print(sqrt(4))
print(pow(3,2))
print(log(10,2))
print(ceil(34.2))
print(floor(34.7))

#working with random module:

from random import *
for i in range(5):
 print(random())

#radint():

from random import *
for i in range(10):
 #print(randint(2,21))
 print(randint(1000,2000))

#uniform():

from random import *
for i in range(10):
 print(uniform(2,21))

#randrange():

 from random import *
for i in range(10):
 print(randrange(2,21,3))

#choice():

l=["sai","mohan","raj","ram",10,34.5,"manoj"]
x=choice(l)
print(x)
print(type(x))

#working with data time modules:

import datetime
x=datetime.datetime.now()
print(x)
from datetime import *
x=datetime.now()
print(x)
print(x.date())
print(x.time())


#example to display current system date and time:

import datetime as dt
x=dt.datetime.now()
print(x)
from datetime import *
x=datetime.now()
print(x)


#strftime() function:

x=datetime.now()
print(x)
print(x.strftime('%A')) 
print(x.strftime('%a'))
print(x.strftime('%Y'))
print(x.strftime('%y'))

#working with calendar module:
from calendar import *
y=1947
m=8
print(month(y,m))
print(month(2021,11))


from calendar import *
print(leapdays(1980,2021))
print(isleap(2020))
print(isleap(2022))












