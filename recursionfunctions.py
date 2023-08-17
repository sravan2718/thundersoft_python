#recursion function:factorial

def factorial(n):
    if (n==1):
        
        return 1
    
    else:
        
        return (n*factorial(n-1))

n=int(input("enter n. value"))
print("number : "+str(n))
print("factorial : "+str(factorial(n)))


#find factorial of number using iterative method

#taking input from the user
num=int(input("enter any number:"))

#storing factorial value in a variable
factorial=1

#check if the number is negative,positive,or zero
if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial=factorial*i
        print("the factorial of",num,"is",factorial)

 
#example:

def factorial (n):
    if (n==1):
     return n
    else:
     return n*factorial(n-1)
n=int(input("enter n. value"))
result=factorial(n)
print(result)
n=5
result=factorial(5)
