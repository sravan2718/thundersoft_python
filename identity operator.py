Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=2
>>> b=2
>>> 
>>> 
>>> print(id(a))
140719572640584
>>> print(id(b))
140719572640584
>>> print(id(a)==id(b))
True
>>> 
>>> a=2
>>> b=3
>>> 
>>> 
>>> print(id(a))
140719572640584
>>> print(id(b))
140719572640616
>>> 
>>> a='mohan'
>>> b='Mohan'
>>> 
>>> 
>>> print(id(a))
2182266493552
>>> print(id(b))
2182266487728
>>> 
>>> print(id(a)==id(b))
False
