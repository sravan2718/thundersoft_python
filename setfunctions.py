#creating a sort
s=set()
print(s)
print(type(s))

#add and update method of set

s=(10,20,30,"sai",45.7,10)
print(s)

s.add(33)
print(s)

s.update([44,55,78,"durga"])
print(s)

#deleting a sort
s=(10,20,30,40,50)
print(s)
del s
print(s)

#set operators:union,intersection,difference,symmetric difference

A={1,2,3,4,5,}
B={4,5,6,7,8}

print(A|B)
print(A.union(B))

print(A&B)
print(A.intersection(B))

print(A-B)
print(A.intersection(B))

print(A-B)
print(A.difference(B))

print(A^B)
print(A.symmetric_difference(B))
 
 #update python set
 companies={'thundersoft','qualcomm'}
 tech_companies=['apple','google''apple']
 companies.update(tech_companies)
 print(companies)


