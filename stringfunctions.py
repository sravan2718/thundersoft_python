#string indexing and slicing

s="hyderabad"
print(s[2:7])
print(s[:6])
print(s[1:1])
print([:])
print(s[0:9:1])
print(s[::-1])
print(s[7:1])
print(s[-1:-5])
print(s[-5:-1])


#string split and max split

s="python is very easy and it is oop and it is interpreter"
print(s)
s1=s.split("",3)
print(s1)
print(type(s1)
      for i in s1:
      print(i)


#string capatalize anfd title

s="python is  very easy"
print (s)
s1=s.capatalize()
print(s1)
print(s.capatalize())
print(s.title())


#sting upper and lower

s="durgasoft"
      print(s)
      print(s.upper())


        s="DURGASOFT"
      print(s)
      print(s.lower())


#string count

s="python is very easy and it is oop and it is interpreter"
      substring="is"
print(s.count(substring))
print(s.count("and"))
print(s.count("is"))
print(s.count("x"))
print(s.count(" "))
print(s.count('a'))

#string replace

s="my name is durga"
print(s)
s1=s.replace("durgs","mohan")
print(s1)


#string join

print(",".join("MOHAN"))
print(" ".join(["sai,mohan,raj,durga"]))

#string reverse

print(" ".join(reversed("SAI")
s="SAI"
print(s[::-1])

#string length

print(len("durgasoft"))

#string startswith,endswith

s="durgasoft"
print(s.startswith('a'))
print(s.startawith('D'))
print(s.startswith('d'))
print(s.endwith('T'))
print(s.endswith('t'))
