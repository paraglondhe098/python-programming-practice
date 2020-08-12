import time
from pygame import mixer
import random

def writelinex(filename, text, line):
    a_file = open(filename, "r")
    list_of_lines = a_file.readlines()
    list_of_lines[line] = f"{text}\n"

    a_file = open(filename, "w")
    a_file.writelines(list_of_lines)
    a_file.close()

def dellines(no):
    number=int(no)
    a_file = open("alarms.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    del lines[number]
    new_file = open("alarms.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()
    a_file = open("alarmt.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    del lines[number]
    new_file = open("alarmt.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def gettime():
    import time
    localtime = time.asctime(time.localtime(time.time()))
    return localtime


def log(x):
    z = open("Mylog.txt", "a")
    z.write("At ")
    z.write(str(gettime()))
    z.write(f":=> {x} \n ")
    z.close()


def music(announcement, mp3, vol, stopword, logname):
    """ >>>>>>This function takes 05 parameters as described below:
        1)announcement (str) - This takes what is to be announced while starting music
        2)mp3 (mp3 filename) - This takes name of the music file.
        3)vol (int) - This takes what should be the volume of the music to be played
        4)stopword (str) - This takes what should be entered to stop the music
        5)logname(str) - Type of activity by which your log is saved"""
    print(announcement)
    mixer.init()
    mixer.music.load(mp3)
    mixer.music.set_volume(vol)
    mixer.music.play()
    print(f"Enter {stopword} to Stop the music")
    while (True):
        z = input()
        if z == stopword:
            mixer.music.stop()
            log(f" {Username} {logname}")
            break
        else:
            print(f"Invalid input ! please Enter {stopword} to Stop music/alarm. ")
            continue


def convint(x):
    z9 = [0, 0, 0]
    z9[0] = int(x[0])
    z9[1] = int(x[1])
    z9[2] = int(x[2])
    return z9


def convert(str):
    zz = str.split(":")
    ss = convint(zz)
    return ss

def convert2(str):
    zz = str.split(":")
    return zz


try:
    samurai=open("alarms.txt","r")
    slices=samurai.readlines()
    samurai.close()
    converted1=map(convert2,slices)
    alarm_title=list(converted1)
except ValueError:
    pass

def alarms(timelist,songname,volume,title):
    import time
    x = 1000
    while(x>0):
        try:
            if time.localtime().tm_hour == timelist[0] and time.localtime().tm_min == timelist[
                1] and time.localtime().tm_sec == timelist[2]:
                music(title, songname, volume, "stop", f"Alarm titled {title}.")
                x = x - 1
                continue
        except IndexError:
            break

def printalarm(list1,list2,no):
    kaka=open("alarms.txt","r")
    sasa=kaka.readlines()
    kaka.close()
    s1=len(sasa)
    joker=0
    i=no
    z=len(list1)-1
    k=len(list2)-1
    while s1>joker:
        try:
            x = list1[z][0]
            y = list2[k]
            print(f"{i})ALARM({x}) = {y}", end="")
            i = i + 1
            z = z - 1
            k = k - 1
            s1=s1-1
            continue
        except IndexError:
            pass


songs=["a.mp3","b.mp3","c.mp3","d.mp3","e.mp3","f.mp3","g.mp3","h.mp3","i.mp3","j.mp3"]
x = 24 * 60 * 60
kaal = open("data.txt")
line = kaal.readlines()  # *)Defaults are:-(For emmergency)
Username = line[0]  # "Parag"
waterhours = int(line[1])  # 30*60
breakfasttime = convert(line[2])  # [9,30,00]
lunchtime = convert(line[3])  # [13,30,00]
dinnertime = convert(line[4])  # [19,00,00]
mouthwashtime = convert(line[5])  # [17,25,00]
starttime = convert(line[6])  # [0,00,00]
blanktime1 = convert(line[7])  # [00,00,00]
blanktime2 = convert(line[8])  # [00,00,00]
ALtitle = line[9]  # "None"v
kaal.close()
zz=open("alarmt.txt","r")
yy=zz.readlines()
zz.close()
converted = map(convert,yy)
alarmlist = list(converted)
warning="If modified settings does not work, then restart the program."
if __name__ == '__main__':
    print("\t*WELCOME TO WATER AND FOOD ALARM SYSTEM*")
    while (True):
        # import time
        time.sleep(0.25)
        print(
            "\n\t1)Enter 1 to start the program \n\t2)Enter 2 to modify settings \n\t3)Enter 0 to view logs \n\t4)Enter x to close")
        time.sleep(0.25)
        inp = input("\n\t=>    ")
        if inp == "1":
            watertime = time.time()
            print("(*)Program started")
            print(f"1)Breakfast time = {breakfasttime[0]}:{breakfasttime[1]}:{breakfasttime[2]}"
                  f"\n2)Lunch time   = {lunchtime[0]}:{lunchtime[1]}:{lunchtime[2]}"
                  f"\n3)Dinner time  = {dinnertime[0]}:{dinnertime[1]}:{dinnertime[2]}"
                  f"\n4)Drink water every {waterhours / 60} minutes.")
            printalarm(alarm_title,yy,5)

            while (x > 0):
                if time.localtime().tm_hour > starttime[0]:
                    if time.localtime().tm_hour == breakfasttime[0] and time.localtime().tm_min == \
                            breakfasttime[1] and time.localtime().tm_sec == breakfasttime[2]:
                        music("Breakfast time !!!", "breakfast.mp3", 0.7, "EAT", "Brakfast taken")
                        x = x - (30 * 60)
                        print("Done!!!")
                        continue
                    if time.localtime().tm_hour == lunchtime[0] and time.localtime().tm_min == lunchtime[
                        1] and time.localtime().tm_sec == lunchtime[2]:
                        music("Lunch time", "lunch.mp3", 0.7, "EAT", "Lunch taken")
                        x = x - (4 * 60 * 60)
                        print("Done!!!")
                        continue
                    if time.localtime().tm_hour == dinnertime[0] and time.localtime().tm_min == dinnertime[
                        1] and time.localtime().tm_sec == dinnertime[2]:
                        music("Dinner time", "dinner.mp3", 0.7, "EAT", "Dinner taken")
                        x = x - (2 * 60 * 600)
                        print("Done!!!")
                        continue
                    if time.localtime().tm_hour == mouthwashtime[0] and time.localtime().tm_min == \
                            mouthwashtime[1] and time.localtime().tm_sec == mouthwashtime[2]:
                        music("Mu dho lo!!!", "mouthwash.mp3", 0.7, "dho liya", "Mouth Washed")
                        x = x - ((3 * 60 * 60) + (30 * 60))
                        print("Done!!!")
                        continue
                    if time.localtime().tm_hour == blanktime1[0] and time.localtime().tm_min == blanktime1[
                        1] and time.localtime().tm_sec == blanktime1[2]:
                        music(ALtitle, "alarm.mp3", 0.7, "STOP", "Alarm")
                        print("Done!!!")
                        continue
                    elif time.time() - watertime >= waterhours:
                        music("Drink water", "water.mp3", 0.7, "Drank", "Drank water")
                        print("Done!")
                        watertime = time.time()
                        continue
                    elif alarms(alarmlist[0], alarm_title[0][2], alarm_title[0][1], alarm_title[0][0]):
                        continue
                    elif alarms(alarmlist[1], alarm_title[1][2], alarm_title[1][1], alarm_title[1][0]):
                        continue
                    elif alarms(alarmlist[2],alarm_title[2][2],alarm_title[2][1],alarm_title[2][0]):
                        continue
                    elif alarms(alarmlist[3],alarm_title[3][2],alarm_title[3][1],alarm_title[3][0]):
                        continue
                    elif alarms(alarmlist[4],alarm_title[4][2],alarm_title[4][1],alarm_title[4][0]):
                        continue
                    elif alarms(alarmlist[5],alarm_title[5][2],alarm_title[5][1],alarm_title[5][0]):
                        continue
                    elif alarms(alarmlist[6],alarm_title[6][2],alarm_title[6][1],alarm_title[6][0]):
                        continue
                    elif alarms(alarmlist[7],alarm_title[7][2],alarm_title[7][1],alarm_title[7][0]):
                        continue
                    elif alarms(alarmlist[8],alarm_title[8][2],alarm_title[8][1],alarm_title[8][0]):
                        continue
                    elif alarms(alarmlist[9],alarm_title[9][2],alarm_title[9][1],alarm_title[9][0]):
                        continue
        if inp == "0":
            zz = open("Mylog.txt")
            zz.read()
            zz.close()
            continue
        if inp == "2":
            alaram=0
            while (True):
                print("_____Input which settings do you want to change?____"
                      "\n1)Enter 1 to change Username"
                      "\n2)Enter 2 to change breakfast-time"
                      "\n3)Enter 3 to change lunch time"
                      "\n4)Enter 4 to change dinner time"
                      "\n5)Enter 5 to change mouth-wash time"
                      "\n6)Enter 6 to change water drinking gap duration"
                      "\n7)Enter 7 to add/view an alarm"
                      "\n8)Enter 8 to set start time"
                      "\n9)Enter 9 to reset to defaults"
                      "\n10)Enter x to exit")
                querry = input("=>")
                if querry == "1":
                    zz = input("Input the new username =>")
                    writelinex("data.txt", zz, 0)
                    print(f"\nYour username is changed from {Username} to {zz} .\n{warning}")
                    time.sleep(0.5)
                    continue
                elif querry == "2":
                    while (True):
                        zz11 = input("Input the new time for breakfast in hh:mm:ss =>")
                        zz1=str(zz11)
                        try:
                            trial = convert(zz11)
                            int(trial[1]) and int(trial[2]) and int(trial[0])
                            writelinex("data.txt", zz1, 2)
                            print(f"Changes saved ! \n{warning}")
                            time.sleep(0.5)
                            break
                        except ValueError:
                            print("Invalid input! try again\n")
                            time.sleep(0.5)
                            continue
                elif querry == "3":
                    while (True):
                        zz22 = input("Input the new time for lunch in hh:mm:ss =>")
                        zz2=str(zz22)
                        try:
                            trial = convert(zz22)
                            int(trial[1]) and int(trial[2]) and int(trial[0])
                            writelinex("data.txt", zz2, 3)
                            print(f"Changes saved ! \n{warning}")
                            time.sleep(0.5)
                            break
                        except ValueError:
                            print("Invalid input! try again")
                            time.sleep(0.5)
                            continue
                elif querry == "4":
                    while (True):
                        zz33 = input("Input the new time for dinner in hh:mm:ss =>")
                        zz3=str(zz33)
                        try:
                            trial = convert(zz33)
                            int(trial[1]) and int(trial[2]) and int(trial[0])
                            writelinex("data.txt", zz3, 4)
                            print(f"Changes saved ! \n{warning}")
                            time.sleep(0.5)
                            break
                        except ValueError:
                            print("Invalid input! try again")
                            time.sleep(0.5)
                            continue
                elif querry == "5":
                    while (True):
                        zz44 = input("Input the new time for mouthwash in hh:mm:ss =>")
                        zz4=str(zz44)
                        try:
                            trial = convert(zz44)
                            int(trial[1]) and int(trial[2]) and int(trial[0])
                            writelinex("data.txt", zz4, 5)
                            print(f"Changes saved ! \n{warning}")
                            time.sleep(0.5)
                            break
                        except ValueError:
                            print("Invalid input! try again")
                            time.sleep(0.5)
                            continue
                elif querry == "6":
                    while (True):
                        zz5 = input("Input the new water drinking duration gap (In minutes)")
                        try:
                            kol = int(zz5) * 60
                            lal = str(kol)
                            writelinex("data.txt", lal, 1)
                            print("Succesfully changed!")
                            time.sleep(0.5)
                            break
                        except ValueError:
                            print("Invalid input! try again")
                            time.sleep(0.5)
                            continue
                elif querry == "9":
                    defaultx = open("data_default.txt", "r")
                    deflist = defaultx.readlines()
                    defaultx.close()

                    defaulty = open("data.txt", "w")
                    defaulty.writelines(deflist)
                    defaulty.close()
                    file = open("alarms.txt", "r+")
                    file.truncate(0)
                    file.write("WakeUP:0.7:a.mp3\n")
                    file.close()
                    file2 = open("alarmt.txt", "r+")
                    file2.truncate(0)
                    file2.write("7:30:00\n")
                    file2.close()
                    print(f"Reset to defaults succesfull.\nIf there are still problems then restart the program")
                    time.sleep(0.5)
                    continue
                elif querry == "x":
                    break
                elif querry == "7":
                    print("What do you want to do?")
                    print("1)Enter 1 to add an alarm \n2)Enter 2 to view alarms \n3)Enter x to remove an alarm")
                    answer=input("=>")
                    if answer=="1":
                        title = input("Enter the alarm title.=>")
                        musicfile = input("Enter the music file name with path or hit enter to choose it automatically.=>")
                        if musicfile=="":
                            musicfile=random.choice(songs)
                            vol = input("How much volume do you want to give for your alarm.(1-10) ")
                            volume = int(vol) / 10
                            alarmo = open("alarms.txt", "a")
                            alarmo.write(f"{title}:{volume}:{musicfile}\n")
                            alarmo.close()
                            while(True):
                                kimm = input("Enter the alarm time in hh:mm:ss =>")
                                try:
                                    trial = convert(kimm)
                                    int(trial[1]) and int(trial[2]) and int(trial[0])
                                    timm = str(kimm)
                                    alarma = open("alarmt.txt", "a")
                                    alarma.write(f"{timm}\n")
                                    alarma.close()
                                    print("Alarm set succesfully.")
                                    time.sleep(0.5)
                                    break
                                except ValueError :
                                    print("Invalid input try again!")
                                    time.sleep(0.5)
                                    continue
                        else:
                            vol = input("How much volume do you want to give for your alarm.(1-10) ")
                            volume = int(vol) / 10
                            alarmo = open("alarms.txt", "a")
                            alarmo.write(f"{title}:{volume}:{musicfile}.mp3\n")
                            alarmo.close()
                            while (True):
                                kimm = input("Enter the alarm time in hh:mm:ss =>")
                                try:
                                    trial = convert(kimm)
                                    int(trial[1]) and int(trial[2]) and int(trial[0])
                                    timm = str(kimm)
                                    alarma = open("alarmt.txt", "a")
                                    alarma.write(f"{timm}\n")
                                    alarma.close()
                                    print("Alarm set succesfully.")
                                    time.sleep(0.5)
                                    break
                                except ValueError:
                                    print("Invalid input try again!")
                                    time.sleep(0.5)
                                    continue
                    if answer=="2":
                        print("Your alarms")
                        printalarm(alarm_title, yy,1)
                        s3=input("\nPress ENTER to go back")
                        time.sleep(0.5)
                        continue
                    if answer=="x":
                        while(True):
                            print("1)Enter x to delete all of the alarms")
                            printalarm(alarm_title, yy, 2)
                            print("Choose the number of alarm do you want to delete.")
                            san = input("=>")
                            print(f"You choose{san}")
                            if san == "x":
                                file = open("alarms.txt", "r+")
                                file.truncate(0)
                                file.close()
                                file2 = open("alarmt.txt", "r+")
                                file2.truncate(0)
                                file2.close()
                                print("Succesfully erased all Alarm data")
                                s3 = input("Press ENTER to go back")
                                time.sleep(0.5)
                                break
                            if san =="2":
                                print("Sorry , You can't delete this alarm!")
                                time.sleep(0.5)
                                continue
                            else:
                                try:
                                    ans = int(san) - 2
                                    dellines(ans)
                                    print("Succesfully deleted")
                                    s3 = input("Press ENTER to go back")
                                    time.sleep(0.5)
                                    break
                                except ValueError and IndexError and IOError:
                                    print("Invalid input! Try again")
                                    time.sleep(1)
                                    continue
                    if answer!="1" and answer!= "2" and answer!="x":
                        print("Invalid input! Try again!")
                        time.sleep(0.5)
                        continue
                elif querry == "8":
                    while (True):
                        xxxx = input("Set your start time in hh:mm:ss =>")
                        xxx=str(xxxx)
                        try:
                            test = convert(xxx)
                            int(test[1]) and int(test[2]) and int(test[0])
                            writelinex("data.txt", xxx, 6)
                            print(f"Changes saved ! \n{warning}")
                            time.sleep(0.5)
                            break
                        except ValueError:
                            print("Invalid input! Try again")
                            time.sleep(0.5)
                            continue
                else:
                    print("Invalid input! try again\n")
                    time.sleep(0.5)
                    continue
        elif inp == "x":
            time.sleep(2)
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print("Invalid input ! try again\n.\n.\n.")
            time.sleep(0.5)
            continue
