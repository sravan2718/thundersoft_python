#example:Try with else clause


#function whichn returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print(c)
#driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


#Example:

# no exception Exception raised in try block
try:
    k = 5//0 #raised divide by Zero exception.
    print(k)

# handles zerodivision 
except ZeroDivisionError:
    print("can't division by zerO")
finally:
    #this block is always excuted
    #regardless of exception generation.
    print('this is always excuted')


#another example:

#program to print the reciprocal of even numbers

try:
    num = int(input("enter a number: "))
    assert num % 2 == 0
except:
    print("not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

# lets see an example:

try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("error denominator cannot be 0.")

finally:
    print("this is finnaly block.")


#examples:try, except, else, finaally blocks:

try:
    x,y = 10, 2
    z =x/y
except ZeroDivisionError:
    print("except zerodivisionerror block")
    print("division by 0 not accepted")
except:
    print('some error occured.')
else:
    print("division = ",z)
finally:
    print("excuting finally block")
    x=0
    y=0
    print("out of try, except, else and finally blocks")

# raise an exception:

x,y=100,2
z=x/2
if z > 10:
    raise valueError(z)
except valueError:
    print(z, "is out of allowed range")
else:
    print(z, "is within the allowed range")


#example:

try:
    raise Exception('spam', 'eggs')
except Exception as inst:                    
      print(type(inst))
      print(inst.args)
      print(inst)


      x, y = inst.args
      print('x =', x)
      print('y =',y)
    
          



