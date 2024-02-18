def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div (x,y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x/y
# Print a user-friendly menu
print("Select operation:")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
# Keep prompting the user until a valid choice is made
while True:
    # Take user input for the choice of operation
    choice= input("Enter choice 1/2/3/4: ")

    if choice in ('1','2','3','4'):
        x=int(input("Enter a value of x: "))
        y=int(input("Enter a value of y: "))
# Perform the selected operation and print the result
        if choice == '1':
            print("result:",add(x,y))
        elif choice == '2':
            print("result",sub(x,y))
        elif choice =='3':
            print("result",mul(x,y))
        elif choice =='4':
            print("result",div(x,y))
            # Exit the loop after a valid operation
        break
    else:
        # Print an error message for invalid input
        print("Invalid input")



