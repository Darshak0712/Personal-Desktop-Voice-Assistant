# Personal-Desktop-Voice-Assistant
---
Hello , I am Darshak creator of this is a personal voice assistant for pc using python.It interacts with user and perform some daily tasks.we can add our shedule tasks that we 
are doing recursively to make it more easier using voice commands. 



---


![Image](https://images.pexels.com/photos/356056/pexels-photo-356056.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260)





## Assistant Skills :

> **`Wikipedia Search : `**
- Say anything that we would like to search by wikipedia just include word wikipedia
  - Example : _`' Jarvis , tell me who is sachin tendulkar as per wikipedia ? '`_

> **`Open Youtube , Google , Whatsapp in browser : `**
- It will open a new tab in browser as like below
  - Example : _`' Hello , Can you open google ? '`_ , _`' Please , Open my whatsapp '` or also we can say simply like`' Open youtube '`_
	
> **`Direct Google or Youtube Search : `**
- We can also open desired result directly , no need to search manually
  - Example :_`' search on google .... '`_ , _`' play fight song on youtube '`_
	
> **`Play Local PC Music Library : `**
- Play music from local folder (already given path) and we have list of music library with index numbers and ask for index numbers and play desired songs as per given index number
  - Example : _`' friend , i feel so tired can you play some music ? '`_
	
> **` Latest Time : `**
- Jarvis can answer us live time includes am / pm as per timings
  - Example : _`' what's time now ? '`_

> **` Opens Installed Softwares : `**
- In this , we can open already installed softwares ...just preset keywords for it and share loacation  with assistant and it will be helpful to open daily use softwares like
  here in my case i have given path for VScode , MSTeams , etc.
  - Example : _`' hi friend , can you open visual studio code for me ? '`_

> **` Microsoft Office : `**
- As like above we can access microsoft office softwares like Microsoft Word , Microsoft PowerPoint , Paint ,etc.
  - Example : _`' i like to make ppt so please open powerpoint '`_ , _`' it's my painting time,let's open paint '`_
 
> **` System Software Tools : `**
- It's also easy task to open sytem tools like task manager , control panel ,etc.
  - Example : _`' let's monitor my system activity so open task manager '`_ , _`' open control panel '`_

> **` Access Gmails Service : `**
- We can send gmails using this assistant but required to apply some settings from our gmail account like third party access ,etc.
  - Example : _`' i want to send gmail '`_
	
> **` Fetch Laptop Battery Usages : `**
- Assistant can chek our laptop's remaing battery and also inform us that it is in plugged in or not. 
  - Example : _`' tell me my laptop's remaing battery '`_	

> **` Sleep Mode : `**
- during this working process in background,just he is waiting for wake up or exit commands and then again he will be ready to accept our queries.for more info see in **More Details**
  - Example : _`' hey, jarvis go to sleep mode '`_	

> **` News Headlines Reading : `**
-  Jarvis can also fetch and read top news headlines for us.
   - Example : _`' jarvis please read some news headlines '`_	

> **` Live Weather Report : `**
-  Fetches live weather information of desired city and will read it 
   - Example : _`' i want weather information '`_	
	 
> **` Funtime Jokes : `**
-  Fun purpose , can tell us jokes 
   - Example : _`' tell me a joke '`_
	 
> **` Computational & Geographical Queries Handling : `**
-  Assistant can directly answer for these computational and geographical questions
   - Example : _`' convert 165 centimeter to feet '`_ or _`' tell me the neighbour countries of India '`_
	 
> **` Sign out/log off : `**
-  lof off from pc  
   - Example : _`' sign out me from this pc '`_	

> **` Shutdown PC : `**
-  To shutdown pc  
   - Example : _`' i feel tired so let's shutdown this '`_	
	 
> **` Restart PC : `**
-  To restart pc  
   - Example : _`' need some refreshments so restart my laptop '`_	


## Libraries Required :
-  Make sure you have successfully installed following libraries before start coding this.
``` python 
import pyttsx3 
import speech_recognition 
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import psutil
import random
import time 
import pywhatkit
import pyjokes
import wolframalpha 
import requests
import subprocess


```

## ThirdParty APIs :

You can get your own API keys from given sites. I have used free plans from there just visit , login and get your unique APi keys and place them in code. Free plans have some
limitations that's why i am not sharing my personal API keys but you can get it very easily from here :

-  [OpenWeatherMap](https://openweathermap.org/api)

-  [WolframAlpha](https://www.wolframalpha.com/)

-  [News API](https://newsapi.org/)

---

![Image](https://images.pexels.com/photos/705164/computer-laptop-work-place-camera-705164.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260)

## More Details :


- On first start up , we get wishese from assistant as per timings like good morning,evening,etc. Basically , after starting waiting for our command and if suppose any reason
  we coudn't say command then don't worry again and again he will ask for query because i have used recursion in command function so if exception occurs the again recall itself 
	for getting our commands.

-  **Smart Query Processing** : I have tried to provide keywords smartly like instead of providing long keywords i have break them in small parts and connected(using and/or) them as per required so even there
   will be any other words in between keywords then also we will not face any problem. for example ,in 'open whatsapp' keyword suppose someone say like 'open my whatsapp' then 
	 it will not work so i have break them like 'open' and 'whatsapp' so both words are required but no problem with words in between them. 

- I have widely used recursion in many places one of them is main function , main function also call itself again and again after our query process so inshort it will not stop 
  untill we desire. But now you will think that if that happen so he will here everythings whatever we said and try to process everything that we don't want. To prevent this i 
	have created sleep mode function.
	
-  Once sleep mode is activated , it's like running process in background and at that time no other commands will process except from wake up or close commands. i will provide source for 
   non-technical people to understand process keywords to start any process by voice assistant.Already examples are given but i'll provide full list of keywords that you may use
	 to perform different taks.

- I know many of you will think that in sleep mode also continuously command input is taking but **difference between sleep and normal** command taking mode is that during sleep mode 
  just taking commands only not processing them for further taks like we are doing in normally.just we can wake up assistant for any other tasks or we can also get exit from here directly
	during sleep mode.Here exit means totally program will stop it's execution and we have to again run manually once to perform new tasks again.

-  i hope now you don't have confusion regarding sleep mode and exit. inshort sleep mode is just like pausing assistant for some time and then we can again activate using speech commands
   but once we have perform exit(**keywords for exit** _`'bye'`_ , _`'stop this'`_,_`'close this'`_,etc. ) then program will stop execution and then we can't use it with directly voice
	 commands untill we run it again.

-  if you have still confusion then you can contact me.


---

 Future Developement Planning :
 ---

-  I will be working on this project to add some extra new features. Also i have some ideas regarding some code modifications and new features to integrate with this like whatsapp automation ,
   sleep mode modifications(auto sleep while continuously command failure), and many more surprises are coming soon.
	 
-  Most welcome for ideas and suggestions from your side because the more we will be together, more better results we can get together. **sharing is caring**😊 






