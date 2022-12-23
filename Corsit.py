import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import os
from ecapture import ecapture as ec
from urllib.request import urlopen
import json
import requests

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py",".pyi"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]
}





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)


engine.setProperty('voices', voices[1].id)


def speak(audio):
     
    engine.say(audio) 
    engine.runAndWait() 

def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("the one and only corsit assisstant in your service Mr. Ojas ")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 

    except Exception as e:
       # print(e)    

        print("Say that again please...")  
        return "None" 
    return query

def countdown(n) :
    while n > 0:
        print (n)
        n = n - 1
    if n ==0:
        print('BLAST OFF!')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('corsitassisstant@gmail.com', 'corsit@123')
    server.sendmail('ojassangra@gmail.com', to, content)
    server.close()

if __name__=="__main__" :
    wishme()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open website' in query:
            webbrowser.open("corsit.sit.ac.in")
  
  
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Aspire\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ojas' in query:
            try:
                speak("What is your message?")
                content = takeCommand()
                to = "ojassangra@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry mujhe maaf krein, i could not do it") 


        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Mr Ojas.")


        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()


        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)


        elif "who am i" in query:
            speak("I think those  who can  talk are humans , but i dont mind calling u a bot instead , as i can also speak .")

        elif "why are you created" in query:
            speak("Thanks to Mr. Ojas. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense ,that destroys all other senses")


        elif "camera" in query or "take a pic" in query:
            ec.capture(0, "corsit Camera ", "img.jpg")


        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you asked me that")
            
        elif "i am fine" in query:
            speak("good to know that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
     

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com") 


        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")


        
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('corsit.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("corsit.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
        elif 'google news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=6e1e50fb76e54ef1af202586dadeb2c7''')
                data = json.load(jsonObj)
                i = 1
                speak('')
                print('''===============Google News============'''+ '\n')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                    print(str(e))

        elif "countdown of" in query:
            query = int(query.replace("countdown of ",""))
            countdown(query)

        elif "weather" in query:
            api_key = "00b7bb8bc26151ed56b82b8299344a0d"

            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name=takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url) 
            x = response.json() 
            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
                speak(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
            else: 
                speak(" City Not Found ")