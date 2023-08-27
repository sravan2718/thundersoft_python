
# even odd index:
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

#except block:

try:
 a = int(input("Enter Num1:"))
 b = int(input("Enter Num2:"))
 print("result is:", a * b)
 print("result is:", a / b)
 print("result is:", a + b)
 print("result is:", a - b)
except ZeroDivisionError as msg:
 print(msg)

#except block multiple:
 
try:
 a = int(input("Enter Num1:"))
 b = int(input("Enter Num2:"))
 print("result is:", a / b)
 print("result is:", a * b)
 print("result is:", a - b)
 print("result is:", a + b)
except ZeroDivisionError as msg:
 print(msg)
except ValueError as msg:
 print(msg)
 
#except block  multiple single:
 
try:
 a = int(input("Enter Num1:"))
 b = int(input("Enter Num2:"))
 print("result is:", a / b)
except(ZeroDivisionError,ValueError)as msg:
 print(msg)
 
#example exception handling:
 
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

#finally example:
    
try:
 print("try block")
except:
 print("except block")
finally:
 print("finally block")


#finally nested :

try:
 print("try block")
except:
 print("except block")
finally:
 print("finally block")

#example:
try:
   result = 1/3
except ZeroDivisionError as err:
   print(err)
else:
   print(f"Your answer is {result}")

#example: 
try:
    a=5
    b='0'
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")

#example:

try:
  a=5
  b='0'
  print(a+b)
except TypeError:
  print('TypeError Occurred')
except:
  print('Some error occurred.')  
print ("Out of try except blocks")

#default except blocks:

try:
  a=5
  b='0'
  print(a+b)
except:
  print('Some error occurred.') 
except TypeError:
  print('TypeError Occurred')
print ("Out of try except blocks")

#multiple except blocks:

try:
    a=5
    b=0
    print (a/b)
except TypeError:
    print('Unsupported operation')
except ZeroDivisionError:
    print ('Division by zero not allowed')
except:
  print('Some error occurred.')
print ('Out of try except blocks')




       












