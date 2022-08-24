
import os
from xml.dom import minicompat
import pyttsx3
from time import sleep
import os
import os.path
from tkinter import *
from tkinter import simpledialog



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)




speak('please enter your username and password to use premium features !')
def get_me():
    root=Tk()
    global sss
    global ppp
    global mee
    sss = simpledialog.askstring("NOVA", "please enter your username")
    ppp = simpledialog.askstring("NOVA", "please enter your  password")
    
    
  

root=Tk()
button = Button(root, text="confirm to enter", command=get_me)
Label(root, text="Enter your username password", bg="#EEEEEE", fg="#555555", font="Times 20 bold underline").pack()
button.pack()
Label(root, text="OR", bg="#EEEEEE", fg="#555555", font="Times 20 bold underline").pack()
exitButton=Button(root, text="click to exit", command=root.destroy).pack()
root.geometry("500x200")
root.mainloop()
global userrrnamme
global passworddd
try:
    userrrnamme=sss
    passworddd=ppp
    print('username is : '+userrrnamme)
    print('password is : '+passworddd)
except:
    speak("okay sir no problem continue")



os.startfile("hortward detection.py")
sleep(300)


