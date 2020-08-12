# Python program to convert
# text to speech

# import the required module from text to speech conversion
import win32com.client

# Calling the Disptach method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")
s = "Hello world"
speaker.Speak(s)

# To stop the program press
# CTRL + Z
# chdir'getcwd', 'getcwdb'listdir
import os
# import permanant
# z=permanant.p_read("mwtimefile")
# print(z)
# import time
# while(True):
#     if time.localtime().tm_hour==19 and time.localtime().tm_min==11 and time.localtime().tm_sec==0:
#         print("Now i false")
#         continue
