
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

# byte from the beginning.
file1.seek(0)
 
print( "Output of Readline function is ")
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
 
file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()


#Appending to a file:

# Append vs write mode
file1 = open("myfile.txt","w")
L = ["This is Delhi \n","This is Paris \n","This is London \n"]
file1.writelines(L)
file1.close()
 
# Append-adds at last
file1 = open("myfile.txt","a")#append mode
file1.write("Today \n")
file1.close()
 
file1 = open("myfile.txt","r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt","w")#write mode
file1.write("Tomorrow \n")
file1.close()
 
file1 = open("myfile.txt","r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()


#example code:
#Create an empty file and write some lines
line1 = 'This is first line. \n'
lines = ['This is another line to store into file.\n',
   'The Third Line for the file.\n',
   'Another line... !@#$%^&*()_+.\n',
   'End Line']
#open the file as write mode
my_file = open('file_read_write.txt', 'w')
my_file.write(line1)
my_file.writelines(lines) #Write multiple lines
my_file.close()
print('Writing Complete')


#example:

line1 = '\n\nThis is a new line. This line will be appended. \n'
#open the file as append mode
my_file = open('file_read_write.txt', 'a')
my_file.write(line1)
my_file.close()
print('Appending Done')



#open the file as read mode:
my_file = open('file_read_write.txt', 'r')
print('Show the full content:')
print(my_file.read())
#Show first two lines
my_file.seek(0)
print('First two lines:')
print(my_file.readline(), end = '')
print(my_file.readline(), end = '')
#Show upto 25 characters
my_file.seek(0)
print('\n\nFirst 25 characters:')
print(my_file.read(25), end = '')
my_file.close()






