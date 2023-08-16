#working of python frozenset:

fruits = frozensets(["apple","banana","orange"])
print(fruits)
fruits.append("pink")
print(fruits)

#python frozenset for tuple:

#passing an empty tuple
nu = ()

#converting tuple to frozenset
fnum = frozenset(nu)

#printing empty frozenset object
print("frozenset object is : ",fnum)

#frozenset for list:

l = ["ram","rom" , "roms"]
fnum = frozenset(l)

#printing empty frozenset object
print("frozenset object is : ",fnum)

#frozenset for dictionary:

#creating a dictionary
student = {"name": "ankit", "age": 21, "sex": "male","college": "giet", "address": "ameedabad"}

#making keys of dictionary as frozenset
key = frozenset(student)

#printing dict keys as frozenset
print('the frozen set is:',key)

#frozenset operations
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozen set
c = A.copy()
print(c)







