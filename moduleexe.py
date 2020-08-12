kumar="                                      <<<<<<<<<<<<< STONE \ PAPER \ SCISSOR >>>>>>>>>>"
print(kumar)
def getdate():
    import time
    localtime = time.asctime(time.localtime(time.time()))
    return localtime

import random
import emoji
import timedelaypy as td
while(True):
    print(
        "**Press 'ENTER' to start the game** \t                      <or>                          **Enter 0 to view scoresheet** ")
    Userentered = input()
    if Userentered=="":
        list1 = {1: "Stone", 2: "Paper", 3: "Scissor"}
        list2 = [1, 2, 3]
        print("Let's play a game of chance with your computer")
        print("      ")
        print("How many matches do you want to play?(Between, [5-15]")
        sa = int(input())
        print("*Choose from the following")
        print("1)1 for Stone"
              "\n2)2 For Paper"
              "\n3)3 For Scissor  ")

        z = sa
        print("......So you have ", sa, " turns.")
        td.tdp()
        print("Your time starts now",end="                                                                                ")
        print("Turns left ",sa,"/",sa)
        Myscore = []
        Compscore = []
        Score = {"Myscore": Myscore, "Compscore": Compscore}
        while z > 0:
            z = z - 1

            inp = input("\t=>")
            i1 = int(inp)
            td.tdp()
            if i1 == 1:
                print("	You choose stone")
            if i1 == 2:
                print("	you choose Paper")
            if i1 == 3:
                print("	You choose Scissor")
            i2 = random.choice(list2)
            td.tdp()
            ic = list1.get(i2)
            print("\tMy choise is", ic)

            td.tdp()
            if i1 == i2:
                print("\tOh! It's tie",
                      end="                                                                                     ")
                print("Turns left ", z, "/", sa)
                Myscore.append(0)
                Compscore.append(0)
                continue
            elif (i1 == 1 and i2 == 3) or (i1 == 2 and i2 == 1) or (i1 == 3 and i2 == 2):
                print("\toh! You won  ",
                      end="                                                                                    ")
                print("Turns left ", z, "/", sa)
                Myscore.append(1)
                Compscore.append(0)
                continue
            else:
                # x = emoji.emojize("\tYah !You loose :duck: !")
                print("\toh! You loose",
                      end="                                                                                    ")
                print("Turns left ", z, "/", sa)
                Myscore.append(0)
                Compscore.append(1)
                continue
        print("\t\t\t_Game Ended_")
        td.tdp()
        print("Time for Score")
        mytotal = sum(Myscore)
        comptotal = sum(Compscore)
        if mytotal > comptotal:
            xxx = emoji.emojize("Hooray :grinning_face_with_big_eyes: you won")
            print(">>>>>Your score = ", mytotal, "/", sa)
            print(">>>>>Computer score = ", comptotal, "/", sa)
            print(".....", xxx)
        elif mytotal < comptotal:
            yyy = emoji.emojize("oh! You loose, i wasn't expected this from you :duck: :duck: :duck:")
            print(">>>>>Your score = ", mytotal, "/", sa)
            print(">>>>>Computer score = ", comptotal, "/", sa)
            print(".....", yyy)
        else:
            zzz = emoji.emojize("Oh! It's tie,:neutral_face: better luck next time!")
            print(">>>>>Your score = ", mytotal, "/", sa)
            print(">>>>>Computer score = ", comptotal, "/", sa)
            print(".....", zzz)
        td.tfp()
        zyz = open("Scoresheet.txt", "a")
        zyz.write("[")
        zyz.write(str(getdate()))
        zyz.write("]                   =>                ")
        zyz.write(str(mytotal))
        zyz.write(" wins in ")
        zyz.write(str(sa))
        zyz.write(" matches.")
        if mytotal > comptotal:
            zyz. write("                Win \n")
            zyz.close()
            break
        elif mytotal< comptotal:
            zyz.write("                Loose \n")
            zyz.close()
            break
        else:
            zyz.write("                Tie \n")
            zyz.close()
            break

    if Userentered=="0":
        Profile=open("Scoresheet.txt")
        zcz=Profile.read()
        print(zcz)
        Profile.close()
        print("Do you want to play now to beat the highscore?(y/n)")
        kay=input("=>")
        if kay=="y":
            print("Let's go")
            print(kumar)
            continue
        if kay=="n":
            td.gobye()
            break
    else:
        print("Invalid Input")
        td.stars()
        continue