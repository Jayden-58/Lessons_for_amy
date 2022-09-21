#Very basic 4 function calculator. It could definately be improved, but its a good starting point for teaching python

def Menu():
    print("Enter the operator you wish to use: (+, -, *, /). Or, enter 'q' to quit")
    operator = input()
    print("Enter the first number for your function")
    first_number = int(input())
    print("enter the second number for your function")
    second_number = int(input())
    if(operator == '+'):
        Add(first_number, second_number)
    elif(operator == '-'):
        Subtract(first_number, second_number)
    elif(operator == '*'):
        Multiply(first_number, second_number)
    elif(operator == '/'):
        Divide(first_number, second_number)
    elif(operator == 'q'):
        exit()
    else:
        print("invalid operator choice. Please try again.")
        Menu()

def Add(first, second):
    print("Adding the numbers...")
    print(first + second)
    Menu()

def Subtract(first, second):
    print("Subtracting the numbers...")
    print(first - second)
    Menu()

def Multiply(first, second):
    print("Multiplying the numbers...")
    print(first * second)
    Menu()

def Divide(first, second):
    print("Dividing the numbers...")
    print(first/second)
    Menu()

Menu()
