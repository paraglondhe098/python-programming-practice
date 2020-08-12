import permanant
import random
import time
from pygame import mixer


def song(announcement,songname,stopword):
    print(announcement)
    mixer.init()
    mixer.music.load(songname)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while (True):
        print(f"Enter {stopword} to Stop the music")
        z = input()
        if z == stopword:
            mixer.music.stop()
            print("I hope you have done your work !")
            break
        else:
            print(f"Invalid input ! please Enter {stopword} to Stop music/alarm. ")
            continue


def reset_to_defaults():
    # Default
    import os
    maindir = os.getcwd()
    dir2 = os.path.join(maindir, "__Permanant_cache__")
    os.chdir(dir2)
    list_of_items=os.listdir
    for items in list_of_items():
        if items.endswith(".pkl"):
            os.remove(items)
    os.chdir(maindir)
    username = "User"
    waterhours = 1800    #1800
    bftime = [9, 30, 0]  #9:30:0
    lutime = [13, 30, 0] #13:30:0
    dintime = [19, 0, 0] #19:0:0
    mwtime = [17, 25, 0] #17:25:0
    permanant.p_add(username, "usernamefile")
    permanant.p_add(waterhours, "waterhoursfile")
    permanant.p_add(bftime, "bftimefile")
    permanant.p_add(lutime, "lutimefile")
    permanant.p_add(dintime, "dintimefile")
    permanant.p_add(mwtime, "mwtimefile")
    print("Reset to default succesfull.")


def display_settings():
    Username_display=permanant.p_read("usernamefile")
    waterhours_display=permanant.p_read("waterhoursfile")
    bftime_display=permanant.p_read("bftimefile")
    lutime_display=permanant.p_read("lutimefile")
    dintime_display=permanant.p_read("dintimefile")
    mwtime_display=permanant.p_read("mwtimefile")
    print(f"1)Username        :  {Username_display}\n"
          f"2)Waterhours      :  {waterhours_display/60}\n"
          f"3)Breakfast Time  :  {bftime_display[0]}:{bftime_display[1]}:{bftime_display[2]}\n"
          f"4)Lunch Time      :  {lutime_display[0]}:{lutime_display[1]}:{lutime_display[2]}\n"
          f"5)Dinner Time     :  {dintime_display[0]}:{dintime_display[1]}:{dintime_display[2]}\n"
          f"6)Mouth wash time :  {mwtime_display[0]}:{mwtime_display[1]}:{mwtime_display[2]}")

def slp():
    time.sleep(0.5)


def csa():
    print("Changes saved succesfully!")


print("\t*WELCOME TO Our programme*")
slp()
print("\n\t1)Enter 1 to start the program \n\t2)Enter 2 to modify settings \n\t3)Enter 0 to view logs \n\t4)Enter x to close")
slp()
inp = input("\n\t=>    ")
if inp=="x":
    time.sleep(2)
    print("Exiting...")
    time.sleep(1)
    exit(1)
elif inp=="o":
    logs=open("Mylog.txt","r")
    read_logs=logs.read()
    logs.close()
elif inp=="2":
    print("Warning !!! Be carefull while modifying settings!")
    print("Your current settings are >>>")
    display_settings()
    print(">>>Enter the number of setting you want to change")
    print(">>>Enter 7 to view/add an alarm")
    print(">>>Enter 8 to reset to defaults")
    print(">>>Enter x to exit")
    inp2=input(" =>")
    if inp2=="1":
        print("Your current username is ",end="")
        print(permanant.p_read("usernamefile"))
        input("Hit enter to continue")
        slp()
        new_username=input("Enter your new username =>")
        permanant.p_add(new_username,"usernamefile")
        csa()
        slp()
    if inp2=="2":
        print("Your current Water-Minutes are ",end="")
        print((permanant.p_read("waterhoursfile"))/60)
        input("Hit enter to continue")
        slp()
        new_waterhours=input("Enter your new Water-Minutes =>")
        new_waterhours=int(new_waterhours)*60
        permanant.p_add(new_waterhours,"waterhoursfile")
        csa()
        slp()
    if inp2=="3":
        print("Your current Breakfast time is ", end="")
        ls=permanant.p_read("bftimefile")
        print(f"{ls[0]}:{ls[1]}:{ls[2]}")
        input("Hit enter to continue")
        slp()
        new_bftime=input("Enter your new Breakfast time (HH:MM:SS)=>")
        new_bftime=new_bftime.split(":")
        permanant.p_add(new_bftime,"bftimefile")
        csa()
        slp()
    if inp2=="4":
        print("Your current Lunch time is ", end="")
        ls=permanant.p_read("lutimefile")
        print(f"{ls[0]}:{ls[1]}:{ls[2]}")
        input("Hit enter to continue")
        slp()
        new_lutime=input("Enter your new Lunch time (HH:MM:SS)=>")
        new_lutime=new_lutime.split(":")
        permanant.p_add(new_lutime,"lutimefile")
        csa()
        slp()
    if inp2=="5":
        print("Your current Dinner time is ", end="")
        ls=permanant.p_read("dintimefile")
        print(f"{ls[0]}:{ls[1]}:{ls[2]}")
        input("Hit enter to continue")
        slp()
        new_dintime=input("Enter your new Dinner time (HH:MM:SS)=>")
        new_dintime=new_dintime.split(":")
        permanant.p_add(new_dintime,"dintimefile")
        csa()
        slp()
    if inp2=="6":
        print("Your current Mouthwash time is ", end="")
        ls=permanant.p_read("mwtimefile")
        print(f"{ls[0]}:{ls[1]}:{ls[2]}")
        input("Hit enter to continue")
        slp()
        new_mwtime=input("Enter your new Mouthwash time (HH:MM:SS)=>")
        new_mwtime=new_mwtime.split(":")
        permanant.p_add(new_mwtime,"mwtimefile")
        csa()
        slp()
    if inp2=="7":
        pass
    if inp2=="8":
        reset_to_defaults()
    if inp2=="x":
        exit(1)
if inp=="1":
    waterminutes=permanant.p_read("waterhoursfile")
    bflist=permanant.p_read("bftimefile")
    lulist=permanant.p_read("lutimefile")
    dilist=permanant.p_read("dintimefile")
    mwlist=permanant.p_read("mwtimefile")
    display_settings()
    watertime=time.time()
    while(True):
        if time.time() - watertime >waterminutes :
            song("Drink water!","water.mp3","Drank")
            watertime=time.time()
            continue
        if time.localtime().tm_hour==bflist[0] and time.localtime().tm_min==bflist[1] and time.localtime().tm_sec==bflist[2] :
            song("Breakfast time","breakfast.mp3","bfDONE")
            continue
        if time.localtime().tm_hour==lulist[0] and time.localtime().tm_min==lulist[1] and time.localtime().tm_sec==lulist[2] :
            song("Lunch time","lunch.mp3","luDONE")
            continue
        if time.localtime().tm_hour==dilist[0] and time.localtime().tm_min==dilist[1] and time.localtime().tm_sec==dilist[2]:
            song("Dinner time","dinner.mp3","dinDONE")
            continue
        if time.localtime().tm_hour==mwlist[0] and time.localtime().tm_min==mwlist[1] and time.localtime().tm_sec==mwlist[2]:
            song("Time for cleanliness","mouthwash.mp3","mwDONE")
            continue
