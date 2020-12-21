# My Python Version 3.7.4

import pyttsx3                       #pip install pyttsx3
import speech_recognition as sr      #pip install speechRecognition
import datetime                      #pip install DateTime
import wikipedia                     #pip install wikipedia
import webbrowser
import os
import smtplib           
import psutil                        #pip install psutil
import random
import time 
import pywhatkit                     #pip install pywhatkit
import pyjokes                       #pip install pyjokes
import wolframalpha                  #pip install wolframalpha
import requests                      #pip install requests
import subprocess

from pprint import pprint       #To print json data format in easy way
from datetime import date
from sound import Sound


MASTER = 'Darshak'
print("Initialize Jarvis...")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



#speak function pronounce paased string text
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This Function wishing wishese as per timings
def wishMe():
    global start_wish_variable

    hour = int(datetime.datetime.now().hour)
    if hour > 10 and hour <= 15:
        speak("Wishing you good noon Master"+MASTER)
    elif hour > 15 and hour <= 19:
        speak("Wishing you good evening "+MASTER)
    elif hour > 20 and hour <= 24:
        speak("Wishing you good Night and sweet dream "+ MASTER)
    else:
        speak("Wishing you a good Day Master " + MASTER )
    start_wish_variable = 1 #checked to switch wish_var_amount so preventing it from every time wish 
    speak("Hi , I am Jarvis , How may i help you ?")

#Sleep mode is feature to continuously run assistant in background and just accept wake up commands only so no further query processing 
def Sleep_Mode():
    speak(f"okay , Good Bye {MASTER}...i am still on to help you....wake up me soon ...")
    speak("Sleep Mode is activated")
    while True: # Infinate Loop untill again wake up 
        query=takeCommand()
        if (("hello" in query) or ("wake up" in query) or ("hey" in query) or ("hi" in query)) and "jarvis" in query:
            speak(f"Welcome Back {MASTER}")
            break
        elif (("stop this" in query) or ("shut up" in query) or ("bye" in query) or ("close this" in query)) and "jarvis" in query:#stop running code and exit from recursion
            speak(f"okay , Good Bye {MASTER}...Enjoy...,Hope to see you soon...")
            start_wish_variable=0
            exit() 
        else:
            print("Waiting for your wake up command...")
    
#Take user input and concerting it to string
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)

    try :
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    
    except Exception as e:
        print("Unable to here clearly , please tell me again....")
        query = takeCommand() #even if for some reason unable to say anything it will run again and again (Recursive calls)
    
    return query.lower()

#send Mails
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail("senderEmail@domainname.com",to,content)
    server.close()

#Specially craeted to remove brackets strings from wikipedia speaking 
def filter_string_brackets(Recieved_String):
    while Recieved_String.count("(") != 0:
        temp=Recieved_String[int(Recieved_String.index("(")):(int(Recieved_String.index(")"))+1):]
        Recieved_String= Recieved_String.replace(temp,"")
    return Recieved_String

#To give some special feature access #Password Protection for any special feature
def password():

    i=3
    while(i>0):
        speak("Please tell me password to access this feature:")
        password = takeCommand()
        # if ' ' in password:
        #     password = int(password.replace(' ',""))
            
        if password.replace(" ","") == str(12345):
            speak("We have recognized your password successfully , you may access that service")
            break
        else:
            i-=1
            speak(f"You have {i} trials remaining , Please say it again")
            
        if i == 0:
            speak("You're out of limit please restart program and try it again")
            exit()
        
#For Direct desired Google Search #Function input and create it ready for google search
def google_query_proscess(rec_query):
    temp_str=""
    for i in rec_query:
        if i == ' ':
            temp_str=temp_str+'+'
        else:
            temp_str=temp_str+i
    return temp_str

#To know for News headlines  #https://newsapi.org/  To find News API 
def NewsHeadlines(): 

	apiKey='Your API Key' #Your API key must be in string format  #Visit above site and take your free API key and paste it here

	# BBC news api #NewsAPI 
	main_url =f"http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={apiKey}"

	# fetching data in json format 
	open_bbc_page = requests.get(main_url).json() 

	# getting all articles in a string article 
	article = open_bbc_page["articles"] 

	# empty list which will 
	# contain all trending news 
	results = [] 
	
	for ar in article: 
		results.append(ar["title"]) 
		
	for i in range(len(results)): 
		
		# printing all trending news 
		print(i + 1, results[i]) 

	#to read the news out loud for us 
	from win32com.client import Dispatch 
	speak = Dispatch("SAPI.Spvoice") 
	speak.Speak(results)				 

# To know about city weather #https://openweathermap.org/api to find Weather API
def Weather():
    try:
        speak("tell me city name to know weather....")
        city=takeCommand()

        apiKey='Your API Key'  #Your API key must be in string format    #Visit above site and take your free API key and paste it here
        url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"

        res=requests.get(url)
        data = res.json() #Recieved whole data from API in json format

        #fetching only Requried Data from API
        temp = data['main']['temp']	
        humidity =data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_description = data['weather'][0]['description']

        # pprint(data) #Tee see all data from API 

        print(f"Temperature : {temp} °C")
        print(f"Weather_description : {weather_description}")
        print(f"Wind-speed : {wind_speed} m/s")
        print(f"Humidity : {humidity} g/m3")
        
        

        speak(f"Temperature : {temp} °C")
        speak(f"Weather description : {weather_description}")
        speak(f"Wind-speed : {wind_speed} meter per second")
        speak(f"Humidity : {humidity} gram per meter qube")
        
        

    except Exception as e:
        speak("coudn't find city weather , Try it again... ")
        print("Couldn't load city data")

#Wolframalpha API for computational and geographical questions #Get Wolframalpha API from https://www.wolframalpha.com/ 
def wolframalpha_query(query):
    apiKey = 'Your API Key'  #Your API key must be in string format   #Visit above site and take your free API key and paste it here
    client = wolframalpha.Client(apiKey)
    try :
            speak("searching for your query...")
            query=query.replace("jarvis","")
            res = client.query(query)
            output = next(res.results).text
            print(output)
            speak(output)
    except Exception as e:
            print("couldn't find solution...")
            speak("I am still in progress and learning New Things and trying to improve myself ,Try it again , hope to see you next time.")



#-----------------------------------------------------------------------------------------------------------------------------------------#


#main function
def main():
    
    global start_wish_variable #Varible for wish func that wish only once during program execution

    NormGreet = ['okay','yes','sure','yeh','Yes, sure','I got it']
    NormGreet = random.choice(NormGreet)+",..."

    if start_wish_variable == 0: 
        # password()                           #To protect any service from strangers' use just uncomment #can place where-ever required 
        speak("Initializing Jarvis...")
        wishMe()

    query = takeCommand()
    OPEN = 'open' in query

    if 'wikipedia' in query:#wikipedia-search
        speak(f'{NormGreet} Searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(filter_string_brackets(results))


    elif OPEN and ('youtube' in query.lower()):#youtube
        speak(f"{NormGreet} Opeing Youtube...")
        firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        firefox.open('https://www.youtube.com')

    elif OPEN and ('google' in query): #google 
        speak(f"{NormGreet} opening google...")
        firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        firefox.open('https://www.google.com')
        
    elif ('search' in query) and ('google' in query):   #direct google search
        speak("Please tell me what do you like to search on google....")
        path_str=google_query_proscess(takeCommand())  #function process input and make it ready for google search url
        firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        firefox.open('https://www.google.com/search?client=firefox-b-d&q='+path_str)



    elif ('play' in query) and ('music' in query.lower()): #play local music library
        speak("Sure , Let's have some music time , Finding Your Music Library...")
        songs_dir = "C:\\Users\\darsh\\Music\\Songs" # local pc path of songs #set your own local path where you have music files
        songs = os.listdir(songs_dir)
        speak("Here's Your Songs List .... Please Tell me index no to play your desire song...")
        
        for i,val in enumerate(songs):#printing all local songs using loop iteration
            print(i+1,val)

        time.sleep(4) #pause time to select index of songs
        speak("Please tell me your Selected Index Number of song:")
        print("Please tell me your Selected Index Number of song:")
        ind =int(takeCommand())
        os.startfile(os.path.join(songs_dir, songs[(ind-1)]))
            
    elif OPEN and 'whatsapp' in query.lower(): #whatsappweb
        speak(f"{NormGreet} Opening Whatsapp")
        firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        firefox.open('https://web.whatsapp.com/')

    elif ('current' in query or 'what\'s' in query)  and 'time' in query.lower():#To chek Timings
        strTime = datetime.datetime.now().strftime("%I:%M:%p")
        speak(f"{MASTER} It's my good time but your time is {strTime}")

    elif OPEN and (('code' in query) or ('vscode' in query) or ('visual studio code' in query.lower())):#VScode
        speak(f"{NormGreet} , Opening Visual Studio Code")
        codePath = "C:\\Users\\darsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    
    elif OPEN and 'task manager' in query.lower(): # Task-Manager
        speak(f"{NormGreet} Opening Task Manager")
        codePath = "C:\\Windows\\System32\\Taskmgr.exe"
        os.startfile(codePath)

    elif OPEN and ('calculator' in query or 'calc' in query):#calculator
        speak(f"{NormGreet} Opening Calculator...")
        codePath = 'C:\\Windows\\System32\\calc.exe'
        os.startfile(codePath)  

    elif OPEN and ('notepad' in query):# Notepad
        speak(f"{NormGreet} Opening Notepad...")
        codePath = 'C:\\Windows\\System32\\notepad.exe'
        os.startfile(codePath)

    elif OPEN and ('wordpad' in query or 'word pad' in query):# WordPad
        speak(f"{NormGreet} Opening Wordpad...")
        codePath = 'C:\\Windows\\System32\\write.exe'
        os.startfile(codePath)

    elif OPEN and ('excel' in query or 'sheets' in query):# Excell
        speak(f"{NormGreet} Opening Excel...")
        codePath = "C:\\Program Files\\WindowsApps\\Microsoft.Office.Desktop.Excel_16051.11901.20218.0_x86__8wekyb3d8bbwe\\Office16\\EXCEL.exe"
        os.startfile(codePath)

    elif OPEN and ('paint' in query):# Paint
        speak(f"{NormGreet} Opening Paint...")
        codePath = "C:\\Windows\\System32\\mspaint.exe"
        os.startfile(codePath)

    elif OPEN and ('team' in query or 'microsoft team' in query):# Microsoft-Teams
        speak(f"{NormGreet} Opening Microsoft Teams...")
        codePath = "C:\\Users\\darsh\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
        os.startfile(codePath)

    elif OPEN and ('word' in query):# Word
        speak(f"{NormGreet} Opening Microsoft Word...")
        codePath = 'C:\\Program Files\\WindowsApps\\Microsoft.Office.Desktop.Word_16051.11901.20218.0_x86__8wekyb3d8bbwe\\Office16\\WINWORD.exe'
        os.startfile(codePath)

    elif OPEN and ('powerpoint' in query or 'power point' in query):# PowerPoint
        speak(f"{NormGreet} Opening Microsoft PowerPoint...")
        codePath = "C:\\Program Files\\WindowsApps\\Microsoft.Office.Desktop.PowerPoint_16051.11901.20218.0_x86__8wekyb3d8bbwe\\Office16\\POWERPNT.exe"
        os.startfile(codePath)
    
    elif 'conrtol' in query or 'panel' in query:#Control Panel
        speak(f"{NormGreet},Opening contol panel...")
        subprocess.Popen('Control Panel')

    elif 'play' in query or 'youtube'in query: #direct youtube search
        song =query.replace('play','')
        speak(f"Playing..."+song)
        pywhatkit.playonyt(song)

    elif 'send gmail' in query.lower(): #required to give permisson from gmail id to use this feature
        try:
            speak("what should i send ? ")
            content=takeCommand()
            to = 'sender@gmail.com'
            sendEmail(to,content)
            speak("Email sent successfully")
            
        except Exception as e:
            print(e)

    elif ('laptop' in query)and'battery' in query.lower(): #chek remaining battery of laptop
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged
        plugged = "Plugged In" if plugged else "Not Plugged In"
        print(f"Hello {MASTER},Your battery is {percent} % and it's in {plugged} condition")
        speak(f"Hello {MASTER},Your battery is {percent} % & It's in {plugged} condition") 

    elif "what\'s up" in query or 'how are you' in query.lower():
            setReplies = ['Just doing some stuff!', 'I am good!',                                     
                        'Nice!', 'I am amazing and full energy to help you']
            speak(random.choice(setReplies))

        
    elif  "go to sleep" in query or 'sleep mode' in query: #Basically infinite loop will ongoing while give keyword to again wakeup
        Sleep_Mode()
    
    elif 'joke' in query: #jokes
        speak(pyjokes.get_joke())

    elif ('thanks' in query) or ('nice' in query) or ('thank you'in query): 
        setReplies = ['It\'s my plessure', 'Welcome','You’re welcome','No problem','No worries','Don’t mention it','My pleasure',
                       'Anytime for you...','It was the least I could do for you...','Glad to help','Sure!','i feel so happy to help you']
        speak(f"{random.choice(setReplies)} ")
        time.sleep(2)
        speak(f"{MASTER} , Tell me what to do next ? what should i do now ?")

    elif ("stop this" in query) or ("shut up" in query) or ("bye" in query) or ("close this" in query.lower()):#stop running code and exit from recursion
        speak(f"okay , Good Bye {MASTER}...Enjoy...,Hope to see you soon...")
        start_wish_variable=0
        exit() 
    
    elif 'news' in query: #NewsHeadlines  
        speak(f"{NormGreet},Here is List of Top Headlines...")
        NewsHeadlines()
    
    elif 'shutdown' in query: #shutdown PC
        speak(f"{MASTER} , Are you sure to shutdown this pc ?")
        query = takeCommand()
        if 'yes'in query or 'ya' in query or 'ye' in query or 'sure' in query or 'confirm' in query:
            speak("okay , Your shutdown process will start in 10 seconds , make sure to save running tasks if required...")
            time.sleep(10)
            os.system("shutdown /s /t 1")
        else:
            speak("shutdown process aborted...")
    
    
    elif 'restart' in query: #Restart PC
        speak(f"{MASTER} , Are you sure to restart this pc ?")
        query = takeCommand()
        if 'yes'in query or 'ya' in query or 'ye' in query or 'sure' in query or 'confirm' in query:
            speak("okay , Your restart process will start in 10 seconds , make sure to save running tasks if required...")
            time.sleep(10)
            os.system("shutdown /r /t 1")
        else:
            speak("restarting process aborted...")

    
    elif "log off" in query or "sign out" in query: #signout from PC
        speak(f"{MASTER} , Are you sure to log out from this pc ?")
        query = takeCommand()
        if 'yes'in query or 'ya' in query or 'ye' in query or 'sure' in query or 'confirm' in query:
            speak("okay , Your sign out process will start in 10 seconds , make sure to save running tasks if required...")
            time.sleep(10)
            subprocess.call(["shutdown", "/l"])
        else:
            pass
    
    elif 'weather' in query:
        Weather()

    else:  #If nothing we get from above then query will move to wolframalpha AIP 
        wolframalpha_query(query)
        
        

    main() # calling main function again untill run exit (Recursive untill exit)
    

#---------------------------------------------------------Main Program--------------------------------------------------------------------#


start_wish_variable = 0 #initialize wish var to clear that it's first time wish during program

#call to main funtion
main() 



