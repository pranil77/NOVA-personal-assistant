import os
import speech_recognition as sr 


def takeCommand():
    #it takes microphone input from user and outputs the string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning ...")
        r.pause_threshold = 0.5
        r.energy_threshold = 800
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print("sorry sir I couldnt recognize it please say that again ")
        return "None"
    return query

while True: 
    wakeup=takeCommand()
    if 'wake up' in wakeup:
        os.startfile("prrrrr.py")