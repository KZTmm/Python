def add(x,y):#Function to perform addition
    return x + y

def sub(x,y):#Function to perform sub
    return x - y

def mul (x,y):#Function to perform mul
    return x * y

def div (x,y):#Function to perform div
    if y == 0:
        return'Cannot divide by zero!'
        
    
    else:
      return x/y
    
x=float(input('Enter your number of x: '))
y=float(input('Enter your number of y: '))

#this code allows you to input two numbers and then performs addition,subtraction,multiplication,and division on those 
#numbers,displaying the result for each operation.

operation=[add,sub,mul,div]
symbols=['+','-','*','/']

for operation,symbols in zip(operation,symbols):
    result=operation(x,y)
    print(f"The value of {x} {symbols} {y} is: {result}")

