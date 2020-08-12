import time
from pygame import mixer
def gettime():
    import time
    localtime = time.asctime(time.localtime(time.time()))
    return localtime
def log(x):
    z=open("Mylog.txt","a")
    z.write("At " )
    z.write(str(gettime()))
    z.write(f":=> {x} \n ")
    z.close()
def music(announcement,mp3,vol,stopword,logname):
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
      z9=[0,0,0]
      z9[0]=int(x[0])
      z9[1]=int(x[1])
      z9[2]=int(x[2])
      return z9
x=24*60*60
# #Defaults
# data=open("data.txt")
Username="Parag"
waterhours=30*60
breakfasttime=[9,30,00]
lunchtime=[13,30,00]
dinnertime=[19,00,00]
mouthwashtime=[17,25,00]
starttime=[0,00,00]
blanktime1=[00,00,00]
blanktime2=[00,00,00]
ALtitle="None"

if __name__ == '__main__':
      print("\t*WELCOME TO WATER AND FOOD ALARM SYSTEM*")
      while(True):
            # import time
            time.sleep(0.25)
            print("\n\n\t1)Enter 1 to start the program \n\t2)Enter 2 to modify settings \n\t3)Enter 0 to view logs \n\t4)Enter x to close")
            time.sleep(0.25)
            inp = input("\n\t=>    ")
            if inp == "1":
                  print("(*)Program started")
                  print(f"1)Breakfast time = {breakfasttime[0]}:{breakfasttime[1]}:{breakfasttime[2]}"
                        f"\n2)Lunch time   = {lunchtime[0]}:{lunchtime[1]}:{lunchtime[2]}"
                        f"\n3)Dinner time  = {dinnertime[0]}:{dinnertime[1]}:{dinnertime[2]}"
                        f"\n4)Drink water every {waterhours / 60} minutes.")
                  if blanktime1==[00,00,00]:
                      pass
                  else:
                      print(f"5)Alarm ({ALtitle}) = {blanktime1[0]}:{blanktime1[1]}:{blanktime1[2]} ")
                  watertime = time.time()
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
            if inp == "0":
                  zz = open("Mylog.txt")
                  zz.read()
                  zz.close()
                  continue
            if inp == "2":
                  while (True):
                        print("_____Input which settings do you want to change?____"
                              "\n1)Enter 1 to change Username"
                              "\n2)Enter 2 to change breakfast-time"
                              "\n3)Enter 3 to change lunch time"
                              "\n4)Enter 4 to change dinner time"
                              "\n5)Enter 5 to change mouth-wash time"
                              "\n6)Enter 6 to change water drinking gap duration"
                              "\n7)Enter 7 to add an alarm"
                              "\n8)Enter 8 to set start time"
                              "\n9)Enter 9 to reset to defaults"
                              "\n10)Enter 10 to exit")
                        querry = input("=>")
                        if querry == "1":
                              zz = input("Input the new username =>")
                              print(f"\nYour username is changed from {Username} to {zz} .\n")
                              time.sleep(0.5)
                              continue
                        elif querry == "2":
                              while(True):
                                    try:
                                          zz1 = input("Input the new time for breakfast in hh:mm:ss =>")
                                          spl = zz1.split(":")
                                          breakfasttime = convint(spl)
                                          print("Changes saved ! \n")
                                          # print(breakfasttime[2])
                                          time.sleep(0.5)
                                          break
                                    except ValueError:
                                          print("Invalid input! try again\n")
                                          continue
                        elif querry == "3":
                              while(True):
                                    try:
                                          zz2 = input("Input the new time for lunch in hh:mm:ss =>")
                                          spl2 = zz2.split(":")
                                          lunchtime = convint(spl2)
                                          print("Changes saved ! \n")
                                          time.sleep(0.5)
                                          break
                                    except ValueError:
                                          print("Invalid input! try again")
                                          continue
                        elif querry == "4":
                              while(True):
                                    try:
                                          zz3 = input("Input the new time for dinner in hh:mm:ss =>")
                                          spl3 = zz3.split(":")
                                          dinnertime = convint(spl3)
                                          print("Changes saved ! \n")
                                          time.sleep(0.5)
                                          break
                                    except ValueError:
                                          print("Invalid input! try again")
                                          continue
                        elif querry == "5":
                              while(True):
                                    try:
                                          zz4 = input("Input the new time for mouthwash in hh:mm:ss =>")
                                          spl4 = zz4.split(":")
                                          breakfasttime = convint(spl4)
                                          print("Changes saved ! \n")
                                          time.sleep(0.5)
                                          break
                                    except ValueError:
                                          print("Invalid input! try again")
                                          continue
                        elif querry == "6":
                              while(True):
                                    try:
                                          zz5 = input("Input the new water drinking duration gap (In minutes)")
                                          waterhours = int(zz5)*60
                                          print("Changes saved ! \n")
                                          time.sleep(0.5)
                                          break
                                    except ValueError:
                                          print("Invalid input! try again")
                                          continue
                        elif querry == "9":
                              Username = "Parag"
                              waterhours = 30 * 60
                              breakfasttime = [9, 30, 00]
                              lunchtime = [13, 30, 00]
                              dinnertime = [19, 00, 00]
                              mouthwashtime = [17, 25, 00]
                              starttime = [9, 00, 00]
                              blanktime1 = [00, 00, 00]
                              blanktime2 = [00, 00, 00]
                              print("Reset to defaults succesfull\n")
                              time.sleep(0.5)
                              continue
                        elif querry == "10":
                              break
                        elif querry == "7":
                              Alarm_title = input("Enter your alarm title.")
                              ALtitle = Alarm_title
                              Altime = input("Input the time for Alarm in hh:mm:ss =>")
                              Altime1 = Altime.split(":")
                              blanktime1 = convint(Altime1)
                              print("Alarm set\n")
                              time.sleep(0.5)
                              continue
                        elif querry=="8":
                              xxx=input("Set your start time in hh:mm:ss =>")
                              zzz=xxx.split(":")
                              starttime=convint(zzz)
                              print("Changes saved ! \n")
                              time.sleep(0.5)
                              break
                        else:
                              print("Invalid input! try again\n")
                              time.sleep(0.5)
                              continue
            elif inp=="x" :
                  time.sleep(2)
                  print("Exiting...")
                  time.sleep(1)
                  break
            else:
                  print("Invalid input ! try again\n.\n.\n.")
                  time.sleep(0.5)
                  continue









