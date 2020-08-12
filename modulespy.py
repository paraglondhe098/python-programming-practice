def getdate():
    import time
    localtime = time.asctime(time.localtime(time.time()))
    return localtime
import time
import random
import emoji
import timedelaypy as td
list1={1:"Stone",2:"Paper",3:"Scissor"}
list2=[1,2,3]
print("<<<<<<<<<<<<< STONE \ PAPER \ SCISSOR >>>>>>>>>>")
print("Let's play a game of chance with your computer")
print("      ")
print("How many matches do you want to play?(Between, [5-15]")
sa=int(input())
print("*Choose from the following")
print("1)1 for Stone"
      "\n2)2 For Paper"
      "\n3)3 For Scissor  ")

z=sa
print("......So you have ",sa," turns.")
td.tdp()
print("Your time starts now")
Myscore = []
Compscore = []
Score = {"Myscore": Myscore, "Compscore": Compscore}
while z>0 :
    z=z-1

    inp = input("\t=>")
    i1  = int(inp)
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
        print("\tOh! It's tie",end="                                                                                     ")
        print("Turns left ", z, "/", sa)
        Myscore.append(0)
        Compscore.append(0)
        continue
    elif (i1 == 1 and i2 == 3) or (i1 == 2 and i2 == 1) or (i1 == 3 and i2 == 2):
        print("\toh! You won  ",end="                                                                                    ")
        print("Turns left ", z, "/", sa)
        Myscore.append(1)
        Compscore.append(0)
        continue
    else:
        x = emoji.emojize("\tYah !You loose :duck: !")
        print(x, end="                                                                               ")
        print("Turns left ", z, "/", sa)
        Myscore.append(0)
        Compscore.append(1)
        continue
print("\t\t\t\t\t\t\t\t\t*Game Ended*")
td.tdp()
print("Time for Score")
mytotal= sum(Myscore)
comptotal=sum(Compscore)
if mytotal>comptotal:
    xxx= emoji.emojize("Hooray :grinning_face_with_big_eyes: you won")
    print(">>>>>Your score = ", mytotal, "/", sa)
    print(">>>>>Computer score = ", comptotal, "/", sa)
    print(".....",xxx)
elif mytotal<comptotal:
    yyy=emoji.emojize("oh! You loose, i wasn't expected this from you :duck: :duck: :duck:")
    print(">>>>>Your score = ", mytotal, "/", sa)
    print(">>>>>Computer score = ", comptotal, "/", sa)
    print(".....",yyy)
else:
    zzz= emoji.emojize("Oh! It's tie,:neutral_face: better luck next time!")
    print(">>>>>Your score = ", mytotal,"/",sa)
    print(">>>>>Computer score = ", comptotal,"/",sa)
    print(".....",zzz)
print("                                                              ",end="    ")
time.sleep(0.40)
print("T", end="")
time.sleep(0.25)
print("H", end="")
time.sleep(0.25)
print("A", end="")
time.sleep(0.25)
print("N", end="")
time.sleep(0.25)
print("K", end="")
time.sleep(0.25)
print("S ", end="")
time.sleep(0.25)
print("F", end="")
time.sleep(0.25)
print("O", end="")
time.sleep(0.25)
print("R ", end="")
time.sleep(0.25)
print("P", end="")
time.sleep(0.25)
print("L", end="")
time.sleep(0.25)
print("A", end="")
time.sleep(0.25)
print("Y", end="")
time.sleep(0.25)
print("I", end="")
time.sleep(0.25)
print("N", end="")
time.sleep(0.25)
print("G", end="")
zyz= open("Scoresheet.txt","a")
zyz.write("[")
zyz.write(str(getdate()))
zyz.write("] => ")
zyz.write(str(mytotal))
zyz.write("/")
zyz.write(str(sa))
zyz.write(". \n")
zyz.close()
