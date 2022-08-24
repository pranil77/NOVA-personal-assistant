import os
import pyttsx3
import speech_recognition as sr 
import datetime
import os
import wikipedia
import webbrowser
from email.message import EmailMessage
from wikipedia.wikipedia import search
import os 
import smtplib
from time import sleep
from instabot import Bot
import os
import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium_stealth import stealth
from pyautogui import click
from tkinter import *
import webbrowser
from os import system
import re
from webdriver_manager.chrome import ChromeDriverManager
#from this import s
from tkinter import simpledialog
import webbrowser





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak(" Good Afternoon sir !")
    elif hour>=17 and hour<18:
        speak("Good Evening")
    speak("nova intelligence online sir .... tell me how may i help ??? ")



def takeCommand():
    #it takes microphone input from user and outputs the string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning ...")
        r.pause_threshold = 0.5
        r.energy_threshold = 5000
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



if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #logic for executing task based on our query 
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)  

        elif 'tell me something about' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)


        elif 'what is' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening youtube")

        elif 'open google.com' in query:
            webbrowser.open("https://www.google.com/")
            speak("opening google")

        elif 'trading' in query:
            webbrowser.open("https://binomoidr.com/trading")
             
        elif 'open hotstar' in query:
            webbrowser.open("https://www.hotstar.com/in")
            speak("opening hotstar")
             
        elif 'show my stock' in query:
            webbrowser.open("https://coindcx.com/trade/BTCUSDT")
            speak("showing currency stocks you buyed")

        elif 'play sidhu moose wala' in query:
            music_dir = 'C:\\Users\\pranil\\Music\\Unlimited Free Music Downloader\\Downloaded Files\\siddhu moosewala'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))

        elif 'party' in query:
            music_dir = 'C:\\Users\\pranil\\Music\\Unlimited Free Music Downloader\\Downloaded Files\\favorate song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'my playlist' in query:
            music_dir = 'C:\\Users\\pranil\\Music\\Unlimited Free Music Downloader\\Downloaded Files\\my playlist'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play marathi song' in query:
            music_dir = 'C:\\Users\\pranil\\Music\\Unlimited Free Music Downloader\\Downloaded Files\\marathi'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("opening whatsapp messaging platform")
        
        elif 'open google meet' in query:
            webbrowser.open("https://meet.google.com/")
            speak("opening google meet")

        elif 'my mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("opening your inbox") 
        
        elif 'send email' in query:
            import smtplib
            email_list = {
            'Bhushan':'bhushanchavan9909@gmail.com',
            'brother':'malharchoudhari399@gmail.com',
            'Nani':'nanichoudhari399@gmail.com',
            'father':'anilrchoudhari@gmail.com',
            'dad':'anilrchoudhari@gmail.com'
            }
            def sendEmail(to,content):
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.login('pranilchoudhari8444@gmail.com','Maruti@123')
                email = EmailMessage()
                email['from'] = 'pranilchoudhari8444@gmail.com'
                email['To'] = to
                email.set_content(content)
                server.send_message(email)
            
            speak("whom do you want to send the email sir ?")
            to=takeCommand()
            to=email_list[to]
            print(to)
            speak("sir what should i say to them")
            content=takeCommand()
            sendEmail(to,content)
            speak("email has been successively sent sir")
            

        elif 'turn off your services' in query:
            speak("okay sir , logging off nova voice assistant ......, nova is offline !")
            break

        elif 'automate whatsapp message' in query:
            try: 
                listo = {'Bhushan':'+919405869990',
                     'pratibha':'+918308842719'}
                import pywhatkit
                speak("to whom you want to send?")
                too=takeCommand()
                too=listo[too]
                print(too)
                speak("what should I say to them ?")
                message=takeCommand()
            except:
                speak('cant find ,please speak the name again')
                listo = {'Bhushan':'+919405869990',
                     'pratibha':'+918308842719'}
                import pywhatkit
                speak("to whom you want to send?")
                too=takeCommand()
                too=listo[too]
                print(too)
                speak("what should I say to them ?")
                message=takeCommand()
            try:
                speak("specify hour")
                time_hour=int(takeCommand())
                speak("specify minute")
                time_minutes=int(takeCommand())
                pywhatkit.sendwhatmsg(too,message,time_hour,time_minutes)    
            except:
                speak('please enter the time again')
                sleep(1)
                speak("specify hour")
                time_hour=int(takeCommand())
                speak("specify minute")
                time_minutes=int(takeCommand())
                pywhatkit.sendwhatmsg(too,message,time_hour,time_minutes)
                
        elif 'search on google' in query :
            speak('what you want to search sir')
            webname=takeCommand()
            PATH="E:\imp\chromedriver_win32\chromedriver.exe"
            driverr = webdriver.Chrome(PATH)
            driverr.get("https://www.google.com/")
            senddd = driverr.find_element_by_name("q")
            senddd.send_keys(webname)
            senddd.send_keys(Keys.RETURN)

        
        
        elif 'open malhar news' in query:
            speak("opening malhar news")
            webbrowser.open("http://malharnews.com/")
        
        elif 'play on youtube' in query:
            speak("what you want to play sir")
            youtubeee=takeCommand()
            webbrowser.open("https://www.youtube.com/results?search_query="+youtubeee)
            speak("okay sir")
            sleep(5)
            click(x=533 , y=431)

        elif 'find a location' in query:
            speak("okay tell me the name")
            location=takeCommand()
            webbrowser.open("https://www.google.com/maps/search/"+location)
            speak('its here sir')



        elif 'search song' in query:
            speak("which one ?")
            songg=takeCommand()
            webbrowser.open("https://open.spotify.com/search/"+songg)

        elif 'search video' in query:
            speak("tell me the name bro")
            video=takeCommand()
            webbrowser.open("https://www.youtube.com/results?search_query="+video)

        elif 'translate sentence' in query:
            speak("from english to which language sir ??")
            translatee=takeCommand()
            if 'Marathi' in translatee:
                speak("ok sir what i have to translate ???")
                translatee1=takeCommand()
                webbrowser.open("https://translate.google.com/?sl=en&tl=mr&text="+translatee1)
            elif 'Spanish' in translatee:
                speak("ok sir what should i translate???")
                translatee1=takeCommand()
                webbrowser.open("https://translate.google.com/?sl=en&tl=es&text="+translatee1)
            elif 'German' in translatee:
                speak("ok sir what should i translate???")
                translatee1=takeCommand()
                webbrowser.open("https://translate.google.com/?sl=en&tl=de&text="+translatee1)
            elif 'French' in translatee:
                speak("ok sir what should i translate ??")
                translatee1=takeCommand()
                webbrowser.open("https://translate.google.co.in/?sl=en&tl=fr&op="+translatee1)

        elif 'search about' in query:
            webbrowser.open("https://www.google.com/search?q="+query)
            speak('ok sir')
        
        elif 'automate instagram' in query:
            bot=Bot()
            instagram_ids={'photography' : 'perfect_captures_7'
                            ,'main':'pranil_choudhari_399'
                            ,'fake' : 'tanishkaaa1717'
                            ,'brother' : 'malhar_choudhari_399'
                            ,'store' : 'reddexstore'}

            speak("which account sir ??")
            idd=takeCommand()
            idd=instagram_ids[idd]
            print(idd)
            
            speak("ok sir , fetching details from your server")  
            bot.login(username= 'pranil_choudhari_399',password='kartik77')
            speak("you are successfully logged in .. What i have to do now ??")
            vola=takeCommand()
        
            if 'upload a photo' in vola:
                speak("which photo you wanna upload sir ??")
                photo=takeCommand().lower
                speak("please provide a caption ??")
                caption=takeCommand()
                bot.upload_photo(photo.jpg , caption)
                webbrowser.open("https://www.instagram.com/"+idd)
                print("photo has been successfully uploaded sir")

        

        elif "open google classroom" in query:
            try:
                PATH="E:\imp\chromedriver_win32\chromedriver.exe"
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_experimental_option("useAutomationExtension", False)
                chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
                driverr = webdriver.Chrome(PATH)
                opt=Options()
                opt.add_argument("start-maximized")
                opt.add_argument("--disable-extensions")
                # Pass the argument 1 to allow and 2 to block
                opt.add_experimental_option("prefs", { \
                    "profile.default_content_setting_values.media_stream_mic": 1,
                    "profile.default_content_setting_values.media_stream_camera": 1,
                    "profile.default_content_setting_values.geolocation": 1,
                    "profile.default_content_setting_values.notifications": 1,
                    "enable_automation":1
                })

                options = webdriver.ChromeOptions()
                options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                options.add_experimental_option('useAutomationExtension', False)
                options.add_argument('--disable-blink-features=AutomationControlled')
                stealth(driverr,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
                opt.add_argument("start-maximized")
                opt.add_argument("--disable-extensions")
                speak('opening google classroom !')
                driverr.get('https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
                username=driverr.find_element_by_xpath('//*[@id="identifierId"]')
                username.click()
                username.send_keys(userrrnamme)

                next=driverr.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
                next.click()
                time.sleep(2)
                password=driverr.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
                password.click()
                password.send_keys(passworddd)
                next=driverr.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
                next.click()
                time.sleep(10)
            except:
                speak("please enter the valid login credentials")    
            try:    
                speak("which class you want to join??")
                classs=takeCommand()
                for i in range(2):
                    if 'operating system' in classs:
                        operatingsystems=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[6]/div/ol/li[2]/div[1]/div[3]/h2/a[1]/div[1]')
                        operatingsystems.click()
                        breakpoint
                    elif 'Java' in classs:
                        javaa=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[6]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]')
                        javaa.click()
                        breakpoint
                    elif 'software testing' in classs:
                        softt=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[6]/div/ol/li[4]/div[1]/div[3]/h2/a[1]')
                        softt.click()
                        breakpoint
                    elif 'web technologies' in classs:
                        webtech=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[6]/div/ol/li[1]/div[1]/div[3]/h2/a[1]')
                        webtech.click()
                        breakpoint
                    elif'Compiler Construction' in classs:
                        compilercons=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[6]/div/ol/li[5]/div[1]/div[3]/h2/a[1]')
                        compilercons.click()
                        breakpoint
            except:
                speak("not found ! , , please say it again !?")
                speak("which class you want to join??")
                classs=takeCommand()
                for i in range(2):
                    if 'operating system' in classs:
                        operatingsystems=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[6]/div/ol/li[2]/div[1]/div[3]/h2/a[1]/div[1]')
                        operatingsystems.click()
                        breakpoint
                    elif 'Java' in classs:
                        javaa=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[6]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]')
                        javaa.click()
                        breakpoint
                    elif 'software testing' in classs:
                        softt=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[6]/div/ol/li[4]/div[1]/div[3]/h2/a[1]')
                        softt.click()
                        breakpoint
                    elif 'web technologies' in classs:
                        webtech=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[6]/div/ol/li[1]/div[1]/div[3]/h2/a[1]')
                        webtech.click()
                        breakpoint
                    elif'Compiler Construction' in classs:
                        compilercons=driverr.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div[1]/div[6]/div/ol/li[5]/div[1]/div[3]/h2/a[1]')
                        compilercons.click()
                        breakpoint    

            breakpoint
        
        elif 'automate google meet' in query:
            def letme():
                root=Tk()
                global sss
                global ppp
                global mee
                global join
                global end 
                mee = simpledialog.askstring("NOVA", "please enter meeting link :")
                join = simpledialog.askstring("NOVA", "please enter joining time in the format = 12:30:00 :")
                end = simpledialog.askstring("NOVA", "please enter meeting ending time in the format = 12:30:00 :")
    
    
  
            root=Tk()
            button = Button(root, text="confirm to enter", command=letme)
            Label(root, text="please enter your meeting code", bg="#EEEEEE", fg="#555555", font="Times 20 bold underline").pack()
            button.pack()
            Label(root, text="OR", bg="#EEEEEE", fg="#555555", font="Times 20 bold underline").pack()
            exitButton=Button(root, text="click to exit", command=root.destroy).pack()
            root.geometry("500x200")
            root.mainloop()
            joiningtime=join
            endingtime=end 
            meetingcode=mee
            print('username is : '+"novassist77@gmail.com")
            print('password is : '+"pranil77")



            def validate_text(regex,inp):
                if not re.match(regex,inp):
                     return False
                return True



            email ="novassist77@gmail.com"
            while not(validate_text(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",email)):
                system("cls")
                print("Invalid Email")

            system('cls')
            psswd = "pranil77"
            system('cls')     
            print("Enter Meeting Code Without Any Special-Character : " , end="")
            code = meetingcode
            while not(validate_text(r"^[a-zA-Z0-9]*$",code)):
                system("cls")
                print("Invalid GMeet Code, Try Again")
                print("Without Special Character")
                code = input()
            system('cls')


            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time)
            print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
            start_time = joiningtime
            while not(validate_text(r"\d\d:\d\d:\d\d",start_time)):
                system("cls")
                print("Enter In Correct Format [ HH:MM:SS ] ")
                print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
                start_time = input()
            print("Time to End Class")
            end_time = endingtime
            while not(validate_text(r"\d\d:\d\d:\d\d",end_time)):
                system("cls")
                print("InCorrect Format, Try Again   [ HH:MM:SS ] ")
                print("Time to End Class")
                end_time = input()


            while current_time != (start_time):
                system("cls")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time , " , Start at : " , start_time)
                sleep(1)

            if current_time == (start_time):
                path = "chromedriver.exe"
                opt = Options()
                # Open With maximized Screen
                opt.add_argument("start-maximized")
                # Add Permission for Microphone , Camera and Notificaion 
                opt.add_experimental_option("prefs", { \
                "profile.default_content_setting_values.media_stream_mic": 1, 
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.notifications": 1 
                })

                driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
                driver.get("https://meet.google.com/new")
                #Email Passed
                search = driver.find_element_by_name("identifier")
                search.send_keys(email)
                search.send_keys(Keys.RETURN)
                driver.implicitly_wait(5)
                #password Passed 
                search = driver.find_element_by_name("password")
                print(search)
                search.send_keys(psswd)
                search.send_keys(Keys.RETURN)

                #Open Google Meet With Your Code
                sleep(3)
                driver.get("https://meet.google.com/lookup/" + code)
                sleep(6)

    
                try:
                    # Turn OFF  Video and Audio 
                    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[4]/div[1]/div/div/div[1]/span/span').click()# Turn OFF Video By Default
                    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]/span/span').click()
                    # Join Class
                    sleep(5)
                    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button/span').click()
                    sleep(20)
                except:
                    print("Can't Join, Try Again")
    

                while current_time != end_time:
                    system("cls")
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Current Time =", current_time , " , End At : " , end_time)
                    sleep(1)

                if current_time == end_time:
                    driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[9]/div[2]/div[2]/div").click()
                    system("cls")
                    print("Left Meet")
                    driver.close()


        elif 'remember that' in query:
            remeberMsg=query.replace("remember that","")
            remeberMsg=remeberMsg.replace("jarvis","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber=open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()
        elif 'what do you remember' in query:
            open ('data.txt', 'r')
            remeber=open('data.txt','r')
            speak("You Tell Me That"+remeber.read())

        elif 'set alarm' in query:
            speak("enter the time")
            time=input("enter the time :")
            while True:
                Time_Ac=datetime.datetime.now() 
                now=Time_Ac.strftime("%H:%M:%S")
                if now == time:
                    music_dir = 'C:\\Users\\pranil\\Music\\Unlimited Free Music Downloader\\Downloaded Files\\favorate song'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
                    sleep(30)
                    speak("Alarm Closed!")
                    breakpoint
                elif now>time:
                    breakpoint