# z=open("data.txt")
# kaka=z.readlines()
# z.close()
# username=kaka[3]
# breakfasttime=[9,30,00]
# lunchtime=[13,30,00]
# dinnertime=[19,00,00]
# mouthwashtime=[17,25,00]
# starttime=[0,00,00]
# blanktime1=[00,00,00]
# blanktime2=[00,00,00]
# ALtitle="None"
# print(username)
# def writelinex(filename,text,line):
#     a_file = open(filename, "r")
#     list_of_lines = a_file.readlines()
#     list_of_lines[line-1] = f"{text}\n"
#
#     a_file = open(filename, "w")
#     a_file.writelines(list_of_lines)
#     a_file.close()
#
# writeliness("data.txt","Parag",4)
# print(username)
# def convint(x):
#     z9 = [0, 0, 0]
#     z9[0] = int(x[0])
#     z9[1] = int(x[1])
#     z9[2] = int(x[2])
#     return z9
# def convert(str):
#     zz= str.split(":")
#     ss=convint(zz)
#     return ss
# sss="12:13:14"
# zzzz=convert(sss)
# print(zzzz[0]+zzzz[1])

# zz=open("aab.txt","r")
# zz1=zz.readlines()
# zz.close()
# print(zz1)
import time
# Username="Parag"
# from pygame import mixer
# def gettime():
#     import time
#     localtime = time.asctime(time.localtime(time.time()))
#     return localtime
# def log(x):
#     z = open("Mylog.txt", "a")
#     z.write("At ")
#     z.write(str(gettime()))
#     z.write(f":=> {x} \n ")
#     z.close()
# def music(announcement, mp3, vol, stopword, logname):
#     """ >>>>>>This function takes 05 parameters as described below:
#         1)announcement (str) - This takes what is to be announced while starting music
#         2)mp3 (mp3 filename) - This takes name of the music file.
#         3)vol (int) - This takes what should be the volume of the music to be played
#         4)stopword (str) - This takes what should be entered to stop the music
#         5)logname(str) - Type of activity by which your log is saved"""
#     print(announcement)
#     mixer.init()
#     mixer.music.load(mp3)
#     mixer.music.set_volume(vol)
#     mixer.music.play()
#     print(f"Enter {stopword} to Stop the music")
#     while (True):
#         z = input()
#         if z == stopword:
#             mixer.music.stop()
#             log(f" {Username} {logname}")
#             break
#         else:
#             print(f"Invalid input ! please Enter {stopword} to Stop music/alarm. ")
#             continue
# def convint(x):
#     z9 = [0, 0, 0]
#     z9[0] = int(x[0])
#     z9[1] = int(x[1])
#     z9[2] = int(x[2])
#     return z9
# def convert(str):
#     zz = str.split(":")
#     ss = convint(zz)
#     return ss
#
# def alarms(timelist):
#     import time
#     x = 1000
#     while(x>0):
#         if time.localtime().tm_hour == timelist[0] and time.localtime().tm_min == timelist[
#             1] and time.localtime().tm_sec == timelist[2]:
#             music("Alarm !!!", "song.mp3", 1, "STOP", "an Alarm ")
#             x=x-1
#             continue
#
#
# # import random
# # names=["kaka","mama","chacha"]
# zz=open("aaaa.txt","r")
# yy=zz.readlines()
# zz.close()
#
# converted = map(convert,yy)
#
# alarmlist = list(converted)
# print(len(alarmlist))

# Alarmstart=map(alarms,alarmlist)
# alarms(alarmlist[1])
# print(time.localtime().tm_hour)
# for items in alarmlist:
#     alarms(items)
# sala=open("aaaa.txt","a")
# sala.write("\n11:12:13")
# sala.close()

# Alarm_title = input("Enter your alarm title.")
#                     writelinex("data.txt", Alarm_title, 9)
#                     while (True):
#                         Altime = input("Input the time for Alarm in hh:mm:ss =>")
#                         try:
#                             test = convert(Altime)
#                             int(test[1]) and int(test[2]) and int(test[0])
#                             writelinex("data.txt", Altime, 7)
#                             print("Alarm set\n")
#                             time.sleep(0.5)
#                             break
#                         except ValueError:
#                             print("Kindly enter the correct info!")
#                             continue
# timm=input("=>")
# alarma = open("aaaa.txt")
# alarma.write(timm)
# alarma.close()

