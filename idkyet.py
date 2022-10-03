balance = 0

def welcome():
    print("Welcome to my app!")
    print("Please enter your name.")
    name = input()
    print("Hello " + name)
    menu()


def menu():
    print("Menu:")
    print("1. deposit")
    print("2. widthdrawl")
    print("3. Check Balance")
    choice = input()
    if(choice == "1"):
        deposit()
        print(" ok")
    elif(choice == "2"):
        #call widthdrrawl function
        print("ok")
    elif(choice == "3"):
        checkbalance()
        print("ok")
    else:
        print("invalid choice, try again.")
        menu()
    

def checkbalance():
    print("checking balance...")
    print("balance: " + str(balance))
    menu()

def deposit():
    print("Enter the amount that you would like to deposit:")
    depositAmount = int(input())
    if(depositAmount >= 0):
        #add
        print()
    menu()

welcome()