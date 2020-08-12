from wfa2 import mouthwashtime
from wfa2 import lunchtime
from wfa2 import dinnertime
from wfa2 import waterhours
from wfa2 import breakfasttime
from wfa2 import starttime
from wfa2 import Username
from wfa2 import blanktime1
from wfa2 import blanktime2
from wfa2 import ALtitle
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
x=24*60*60
watertime=time.time()
while (x>0):
    if time.localtime().tm_hour > starttime[0]:
        if time.localtime().tm_hour==breakfasttime[0] and time.localtime().tm_min==breakfasttime[1] and time.localtime().tm_sec==breakfasttime[2]:
            music("Breakfast time !!!","breakfast.mp3",0.7,"EAT","Brakfast taken")
            x=x-(30*60)
            print("Done!!!")
            continue
        if time.localtime().tm_hour==lunchtime[0] and time.localtime().tm_min==lunchtime[1] and time.localtime().tm_sec==lunchtime[2]:
            music("Lunch time","lunch.mp3",0.7,"EAT","Lunch taken")
            x=x-(4*60*60)
            print("Done!!!")
            continue
        if time.localtime().tm_hour==dinnertime[0] and time.localtime().tm_min==dinnertime[1] and time.localtime().tm_sec==dinnertime[2]:
            music("Dinner time","dinner.mp3",0.7,"EAT","Dinner taken")
            x=x-(2*60*600)
            print("Done!!!")
            continue
        if time.localtime().tm_hour==mouthwashtime[0] and time.localtime().tm_min==mouthwashtime[1] and time.localtime().tm_sec==mouthwashtime[2]:
            music("Mu dho lo!!!","mouthwash.mp3",0.7,"dho liya","Mouth Washed")
            x =x- ((3 * 60 * 60) + (30 * 60))
            print("Done!!!")
            continue
        if time.localtime().tm_hour==blanktime1[0] and time.localtime().tm_min==blanktime1[1] and time.localtime().tm_sec==blanktime1[2]:
            music(ALtitle,"alarm.mp3",0.7,"STOP","Alarm")
            print("Done!!!")
            continue
        elif time.time() - watertime >= waterhours:
            music("Drink water", "water.mp3", 0.7, "Drank", "Drank water")
            print("Done!")
            watertime = time.time()
            continue

