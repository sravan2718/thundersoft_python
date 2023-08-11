if:
syntax:if condition:
           statements 
i=100
if i==100:
print("true")

 
if else:
 
syntax:if condition:
       statements
    else:
   statements


i=100
if i==100:
    print("true")
else:
    print("false")


nested if:

syntax:if condition:
            statements
     else:
      if condition:
           statements
     else:
       statements

i=int(input("Enter num1:"))
j=int(input("Enter num2:"))
if(i>j):
    print(i,"is greater than ",j)
else:
    if(i<j):
        print(i,"is less than",j)
    else:
        print(i,"is equal to",j) 

elif:
   
syntax:if condition1:
             statements
        elif confdition2:
             statememnts
        elif condition3:
              statements
        else:
              statements 
    
n=int(input("Enter number:"))
if n==1:
   print("ONE")
elif n==2:
   print("TWO")
elif n==3:
   print("THREE")
elif n==4:
   print("FOUR")
else:
   print("Invalid number")

        

