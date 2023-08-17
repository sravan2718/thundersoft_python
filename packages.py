#python packages

def pots():
    print("I'm pots phone")

#now import your phone package

import phone
phone.pots()
phone.Isdn()
phone.G3()

#simple package

from simple_package import a,b
a.bar()
b.foo()

import simple_package
simple_package.a.bar()
simple_package.b.foo()


#package module

def gfg():
    print("welcome to gfg")
def sum(a, b):
    return a+b
from .mod1 import gfg
from .mod2 import sum

from mypackage import mod1
from mypackage import mod2

mod1.gfg()
res = mod2.sum(1, 2)
print(result)
