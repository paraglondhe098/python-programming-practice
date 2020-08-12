Username="User"
import time
# import random
from pygame import mixer
def gettime():
    import time
    localtime = time.asctime(time.localtime(time.time()))
    return localtime
def log(x):
    z=open("Health.txt","a")
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
            print(f"Invalid input ! please Enter {stopword} to Stop music. ")
            continue
watertime=time.time()
eyetime=time.time()
exetime=time.time()
waterzone=27*60
eyezone=30*60
exezone=45*60
while(True):
    if 17>=time.localtime().tm_hour >=9 :
        while(True):
            if time.time() - watertime >= waterzone:
                music("Drink water", "water.mp3", 0.7, "Drank", "Drank water")
                print("Done!")
                watertime = time.time()
                continue
            if time.time() - eyetime >= eyezone:
                music("Eye Exercise", "eyes.mp3", 0.7, "EyDone", "Done eye Exercise")
                print("Done!")
                eyetime = time.time()
                continue
            if time.time() - exetime >= exezone:
                music("Exercise time", "physical.mp3", 0.7, "ExDone", "Done Physical Exercise")
                print("Done!")
                exetime = time.time()
                continue
    if time.localtime().tm_hour == 17 and time.localtime().tm_min == 00 and time.localtime().tm_sec >0:
            print("Exiting Program")
            break

