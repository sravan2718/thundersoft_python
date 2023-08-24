

# write data in a file.
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
 
# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close() #to change file access modes
 
file1 = open("myfile.txt","r+")
 
print("Output of Read function is ")
print(file1.read())

print()
 
file1.seek(0)



# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
 
file1.seek(0)
 
print("Output of Readline(9) function is ")
print(file1.readline(9))
 
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()

# read data from a file.
 
# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes
ile1 = open("myfile.txt", "r+")
 
print("Output of Read function is ")
print(file1.read())
print()
 
# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)
rint("Output of Readline function is ")
print(file1.readline())
print()
 
file1.seek(0)
 
# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()
 
file1.seek(0)
 
print("Output of Readline(9) function is ")
print(file1.readline(9))
print()
 
file1.seek(0)
print("Output of Readline function is ")
print(file1.readline())
print()
 
file1.seek(0)
 
# read data from a file.
 
# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes
 
file1 = open("myfile.txt", "r+")
 
print("Output of Read function is ")
print(file1.read())
print()
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()


#open file operations:

# opening a file
 
 
# Open function to open the file "myfile.txt"
# (same directory) in read mode and store
# it's reference in the variable file1
 
file1 = open("myfile.txt")
 
# Reading from file
print(file1.read())
 
file1.close()

#example:
 # (same directory) in append mode and store
# it's reference in the variable file1
file1 = open("myfile.txt" , "a" )
 
# Writing to file
file1.write("\nWriting to file:)" )
 
# Closing file
file1.close()

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name

# Close opend file
fo.close()


# Open a file
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n")

# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print "Read String is : ", str

# Check current position
position = fo.tell()
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10)
print "Again read String is : ", str
# Close opend file
fo.close()



