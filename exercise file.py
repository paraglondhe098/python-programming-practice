print("#>>>>>Welcome to health management system<<<<<<#")
while(True):
    def getdate():
        import datetime
        return datetime.datetime.now()


    print("What is your client name?")
    print(" 1) 1 For Harry"
          "\n 2) 2 For Rohan"
          "\n 3) 3 For Hammad ")
    try:
        x = int(input("=>"))
    except ValueError:
        print(4 * "*")
        print(3 * "*")
        print(2 * "*")
        print("*")
        print("Invalid input! try again")
        continue
    print("What do you want to do with this profile ?")
    print(" 1) 1 For Lock something"
          "\n 2) 2 For View something")
    try:
        y = int(input("=>"))
    except ValueError:
        print(4 * "*")
        print(3 * "*")
        print(2 * "*")
        print("*")
        print("Invalid input! try again")
        continue
    print("What do you want to view/lock ?")
    print(" 1) 1 For View/lock Diet"
          "\n 2) 2 For View/lock Exercise")
    try:
        z = int(input("=>"))
    except ValueError:
        print(4 * "*")
        print(3 * "*")
        print(2 * "*")
        print("*")
        print("Invalid input! try again")
        continue
    if x == 1 and y == 1 and z == 1:
        Harry = open("Harrydiet.txt", "a")
        harrydiet = input("Enter the diet name.=>")
        Harry.write("[")
        Harry.write(str(getdate()))
        Harry.write("] => ")
        Harry.write(harrydiet)
        Harry.write(". \n")
        Harry.close()
        print("Locked succesfully...")
        print("Lock more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 2 and y == 1 and z == 1:
        Rohan = open("Rohandiet.txt", "a")
        Rohandiet = input("Enter the diet name.=>")
        Rohan.write("[")
        Rohan.write(str(getdate()))
        Rohan.write("] => ")
        Rohan.write(Rohandiet)
        Rohan.write(". \n")
        Rohan.close()
        print("Locked succesfully...")
        print("Lock more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 3 and y == 1 and z == 1:
        Hammad = open("Hammaddiet.txt", "a")
        Hammaddiet = input("Enter the diet name.=>")
        Hammad.write("[")
        Hammad.write(str(getdate()))
        Hammad.write("] => ")
        Hammad.write(Hammaddiet)
        Hammad.write(". \n")
        Hammad.close()
        print("Locked succesfully...")
        print("Lock more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 1 and y == 1 and z == 2:
        Harrye = open("Harryexe.txt", "a")
        harryexe = input("Enter the exercise name.=>")
        Harrye.write("[")
        Harrye.write(str(getdate()))
        Harrye.write("] => ")
        Harrye.write(harryexe)
        Harrye.write(". \n")
        Harrye.close()
        print("Locked succesfully...")
        print("Lock more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 2 and y == 1 and z == 2:
        Rohane = open("Harryexe.txt", "a")
        Rohanexe = input("Enter the exercise name.=>")
        Rohane.write("[")
        Rohane.write(str(getdate()))
        Rohane.write("] => ")
        Rohane.write(Rohanexe)
        Rohane.write(". \n")
        Rohane.close()
        print("Locked succesfully...")
        print("Lock more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 3 and y == 1 and z == 2:
        Hammade = open("Hammadexe.txt", "a")
        Hammadexe = input("Enter the exercise name.=>")
        Hammade.write("[")
        Hammade.write(str(getdate()))
        Hammade.write("] => ")
        Hammade.write(Hammadexe)
        Hammade.write(". \n")
        Hammade.close()
        print("Locked succesfully...")
        print("Lock more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 1 and y == 2 and z == 1:
        Reahardie = open("Harrydiet.txt")
        #k = int(input("Enter which line do you want to read? =>"))
        pop=Reahardie.read()
        print("*___________Diet info of Harry____________*")
        print("|      Date & Time           => Food Taken|")
        print(pop)
        print("___________________________________________")
        Reahardie.close()
        print("View more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 1 and y == 2 and z == 2:
        Reaharexe = open("Harryexe.txt")
        #k = int(input("Enter which line do you want to read? =>"))
        bob=Reaharexe.read()
        print("*_______Exercise info of Harry____________*")
        print("|      Date & Time           => Exercise  |")
        print(bob)
        print("___________________________________________")
        Reaharexe.close()
        print("view more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 2 and y == 2 and z == 1:
        Rearohdie = open("Rohandiet.txt")
        #k = int(input("Enter which line do you want to read? =>"))
        knob=Rearohdie.read()
        print("*___________Diet info of Rohan____________*")
        print("|      Date & Time           => Food Taken|")
        print(knob)
        print("___________________________________________")
        Rearohdie.close()
        print("view more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 2 and y == 2 and z == 2:
        Rearohexe = open("Rohanexe.txt")
        #k = int(input("Enter which line do you want to read? =>"))
        hip=Rearohexe.read()
        print("*_______Exercise info of Rohan____________*")
        print("|      Date & Time           => Exercise  |")
        print(hip)
        print("___________________________________________")
        Rearohexe.close()
        print("view more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 3 and y == 2 and z == 1:
        Reahamdie = open("Hammaddiet.txt")
        #k = int(input("Enter which line do you want to read? =>"))
        hop=Reahamdie.read()
        print("*___________Diet info of Hammad____________*")
        print("|      Date & Time           => Food Taken|")
        print(hop)
        print("___________________________________________")
        Reahamdie.close()
        print("view more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    elif x == 3 and y == 2 and z == 2:
        Reahamexe = open("Hammadexe.txt")
        #k = int(input("Enter which line do you want to read? =>"))
        tik=Reahamexe.read()
        print("*_______Exercise info of Hammad____________*")
        print("|      Date & Time           => Exercise  |")

        print(tik)
        print("___________________________________________")
        Reahamexe.close()
        print("view more (y/n) ?")
        kaka = input()
        if kaka == "y":
            print("Let's go!!!")
            continue
        if kaka == "n":
            print("Exiting")
            print("Bye")
            print(4 * "*")
            print(3 * "*")
            print(2 * "*")
            print("*")
            break
    else:

        print(4 * "*")
        print(3 * "*")
        print(2 * "*")
        print("*")
        print("Invalid input ! try again")
        continue





