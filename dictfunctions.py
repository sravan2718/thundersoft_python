#creating a dictionary

d={}
print(d)
print(type(d))

d={"eid":1234,"ename":"sai"}
print(d)


#Acess value from dic

d={"eid":1234,"ename":"sai"}
print(d)

print(d["ename"])
print(d.get("ename"))

print(d.get("age"))


#deleting a dict

d={"eid":123,"ename":"sai"}
print(d)
del d["ename"]
print(d)


#dic copy

d={1:"sai",2:"mohan",3:"raja"}
print(d)
d1=d.copy()
print(d1)
d[1]="durga"
print(d)
print(d1)
print(id(d1))
print(id(d))

#dic items,values,keyfunctions

d={1:"sai",2:"mohan",3:"raja"}
print(d)
print(d.items())
print(d.keys())
print(d.values())


#dict len and membership test

d={1:"sai",2:"mohan",3:"raja"}
print(1 in d)
print("sai" in d)
print(len(d))


#dict pop and pop item methods

d={1:"sai",2:"raja",3:"mohan"}
print(d)
print(d.popitem())
print(d)








