#Faulty calculator
print("*Welcome to my calculator*")
print("Enter your two numbers : ")
print("No.1 =")
No1=input()
try:    int(No1)
except ValueError :
    print("Invalid input")
    exit(1)
print("No.2 =")
No2=input()
try:    int(No2)
except ValueError :
    print("Invalid input")
    exit(1)
print("choose your operator + , - , * , or /")
op=input()
try:
    if op == "+" or "-" or "*" or "/":
        if int(No1) == 45 and int(No2) == 3 and op == "*":
            print("Answer is 555")
        elif int(No1) == 56 and int(No2) == 9 and op == "+":
            print("Answer is 77")
        elif int(No1) == 56 and int(No2) == 6 and op == "/":
            print("Answer is 555")
        else:
            if op == "*":
                Multiplication = int(No1) * int(No2)
                print("Answer is", Multiplication)
            elif op == "+":
                Addition = int(No1) + int(No2)
                print("Answer is", Addition)
            elif op == "-":
                Substraction = int(No1) - int(No2)
                print("Answer is", Substraction)
            elif op == "/":
                Division = int(No1) / int(No2)
                print("Your answer is",Division)
    else:
        print("Enter correct info !")
except ZeroDivisionError:
    print("Can't Divide by zero")
#print("Do you want to continue? ...(y/n) ")
#lollo=input()
#if lollo=="n"
#    print("Exiting, see you again :)")
# else:
