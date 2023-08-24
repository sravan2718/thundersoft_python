
#open file example:

f=open("sample.txt","w")
print("file name is:",f.name)
print("file mode is:",f.mode)
print("is file readable?",f.readable())
print("is file writable?",f.writable())
print("is file closed?",f.closed)
f.close()
print("is file closed?",f.closed)

# providing mode to open()

# opens the file in reading mode
f = open("path_to_file", mode='r')

# opens the file in writing mode 
f = open("path_to_file", mode = 'w')

# opens for writing to the end 
f = open("path_to_file", mode = 'a')


# example:

created_file = open("geeksforgeeks.txt","x")
 
# Check the file
print(open("geeksforgeeks.txt","r").read() == False)

# example:

my_file = open("geeksforgeeks.txt","a")
my_file.write("..>>Visit geeksforgeeks.org for more!!<<..")
my_file.close()
 
# reading the file
my_file = open("geeksforgeeks.txt","r")
print(my_file.read())

#example:
#write  file operation:
f = open("C:text.txt","w")#overrite my statements
print(f.write("this will overrite everything"))
print(f.write("Hello , this is puneeth onboarded in thundersoft to pursue my internship"))

f = open("C:text.txt","r")
for x in f:
    print(x)
    
#write function:
f=open("sample.txt",'w')
l=["sai\n","ram\n","mohan\n","durga\n"]
f.writelines(l)
print("List data written to the file")
f.close()

#example:
f = open("C:text.txt","a")
print(f.write("This is the appending statement"))

f = open("C:text.txt","r")
for x in f:
    print(x)


# writing to file:
 
# Opening a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
 
# Writing a string to file
file1.write(s)
 
# Writing multiple strings
# at a time
file1.writelines(L)

#Closing file
file1.close()
 
# Checking if the data is
# written to file or not
file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()
 




