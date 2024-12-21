print("Welcome to the Command-Line Calculator!")
def add():

    try:
        print("Input 0 for stop adding and get the answer.")
        uinput=float(input("Enter the number:"))
        total=0
        while(uinput!=0):
            total=total+uinput
            uinput=int(input("Enter the number:"))
    except:
        print("You can't input special characters or letters")
    return total
def sub():
    try:
        print("Input 0 for stop subtracting and get the answer.")
        uinput1 = float(input("Enter the number:"))
        uinput2 = float(input("Enter the number:"))
        total = uinput1-uinput2
        while (uinput != 0):
            uinput = int(input("Enter the number:"))
            total = total - uinput
    except:
        print("You can't input special characters or letters")
    return total

def divide():
    try:
        print("Input 0 for stop dividing and get the answer.")
        uinput1 = float(input("Enter the number:"))
        uinput2 = float(input("Enter the number:"))
        total = uinput1/uinput2
    except:
        print("You can't input special characters or letters")
    return total

def mul():
    try:
        print("Input 0 for stop multiplying and get the answer.")
        uinput1 = float(input("Enter the number:"))
        uinput2 = float(input("Enter the number:"))
        total = uinput1*uinput2
    except:
        print("You can't input special characters or letters")
    return total

while True:
    print("Select a operation:")
    print("ADD: +")
    print("Subtract: -")
    print("Divide: /")
    print("Multipy: *")
    opin=input("Input operation here:")
    if (opin == "+"):
        answer = add()
    elif (opin=="-"):
        answer=sub()
    elif(opin=="/"):
        answer=divide()
    elif(opin=="*"):
        answer=mul()
    else:
        answer="Invalid input!"
    print("Answer is:"+str(answer))