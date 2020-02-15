import speech_recognition as sr
import pyttsx3
import re #split text
import datetime #current date and time
import random #for random function
import time
import requests, json
from pygame import mixer
#import serial as sl

engine = pyttsx3.init()
#ser = sl.Serial('COM22', 9600)

api_key = "fa862172403ad7caf125160be68be451"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "namaste")

GREETING_RESPONSES = ["Yo!", "hey", "hi", "hello",]

moodq = ["happy", "nice", "good", "awesome", "fine"]
moodr = ["Oh! thats very good", "I am also like you", "good thing"]
moods = ["sad", "bad", "very sad","not good"]

ownerq = ["who made you", "who is you owner", "who is your head", "to whom you belong"]
ownera = ["Founders of HP", "HP Team", "Brand of my Laptop"]

laughq = ["laugh", "joke"]
laugha = ["Did you hear about the blind carpenter who picked up his hammer and saw?", "A teacher is talking to a student.Teacher: Did your father help you with your homework? Student: No, he did it all by himself.","On a crowded bus, one man noticed that another man had his eyes closed. What's the matter? Are you sick? No, I'm okay. It's just that I hate to see an old lady standing."]

nameq = ["call me","my name is"]

dateq = ["date", "time"]

def speak(spea):
    engine.say(spea)
    engine.runAndWait()

def check_for_greeting(sentence, i):
    for i in range(0,6):
        if GREETING_KEYWORDS[i] in sentence:
            data1 = random.choice(GREETING_RESPONSES)
            print(data1)
            speak(data1)
            print("How are you?")
            speak("How are you?")
            
    for i in range(0,5):
        if moodq[i] in sentence:
            data1 = random.choice(moodr) + ",It would be great to talk with you"
            print(data1)
            speak(data1)
            print("Now, What you want me to do")
            speak("Now, What you want me to do")

    for i in range(0,3):
        if sentence == moods[i]:
            print("Why?"," ","How can I Help?")
            speak("Why?"," ","How can I Help?")

    if sentence == "calculator":
        print("Tell me numbers: ")
        #speak("Tell me numbers: ")
        a=int(input())
        b=int(input())
        print("Tell me what you want: ", "\r", "1: add", "\r", "2: subtract", "\r", "3: multiply", "\r", "4: divide")
        #speak("Tell me what you want: ", "\r", "1: add", "\r", "2: subtract", "\r", "3: multiply", "\r", "4: divide")
        j=input()

        if j == 1 or "add":
            print(a+b)

        elif j == 2 or "subtract":
            print(a-b)

        elif j == 3 or "multiply":
            print(a*b)

        elif j == 4 or "divide":
            if b != 0:
                print(a/b)

    if "song" in sentence:
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print("What type of song you want?")
                speak("What type of song you want?")
                audio = r.listen(source)
        j = r.recognize_google(audio)
        j = j.lower()
        if "hindi" in j:
            mixer.init()
            mixer.music.load('hindi.mp3')
            mixer.music.play()
            time.sleep(30)
        elif "punjabi" in j:
            print("You shound go for djpunjab.com or pagaljatt.com")
            speak("You shound go for djpunjab.com or pagaljatt.com")
        elif "english" in j:
            mixer.init()
            mixer.music.load('english.mp3')
            mixer.music.play()
            time.sleep(30)
        else:
            print("Search it on google","\r","I know about only english, hindi, punjabi")
            speak("Search it on google","\r","I know about only english, hindi, punjabi")
    
    for i in range (0,4):
        if sentence == ownerq[i]:
            data1 = random.choice(ownera)
            print(data1)
            speak(data1)

    for i in range(0,2):
        if laughq[i] in sentence:
            data1 = random.choice(laugha)
            print(data1)
            speak(data1)
            
    if nameq[0] in sentence:
        splitted = sentence.split()
        a=splitted[2]
        data1 = random.choice(GREETING_RESPONSES) + " " + a
        print(data1)
        speak(data1)
        
    if nameq[1] in sentence:
        splitted=sentence.split()
        a=splitted[3]
        data1 = random.choice(GREETING_RESPONSES) + " " + a
        print(data1)
        speak(data1)

    for i in range(0,2):
        if dateq[i] in sentence:
            now=datetime.datetime.now()
            print("Current date and time: ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))

    if("led" in sentence):
        if("one" in sentence or "first" in sentence):
            if("on" in sentence):
                print("Led first on")
                speak("Led first on")
                #ser.write('c'.encode())
            elif("off" in sentence):
                print("Led first off")
                speak("Led first off")
                #ser.write('d'.encode())
        elif("second" in sentence or "two" in sentence):
            if("on" in sentence):
                print("Led second on")
                speak("Led second on")
                #ser.write('e'.encode())
            elif("off" in sentence):
                print("Led second off")
                speak("Led second off")
                #ser.write('f'.encode())

    if("weather" in sentence):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try: 
                print("which city")
                speak("which city")
                audio = r.listen(source, timeout = 3)
            except Exception as e:
                print("Error: ", e)
                audio = ""
        try: 
            city_name = r.recognize_google(audio)
            city_name = city_name.lower()
        except Exception as e:
            print("Error: ", e)
            city_name = ""
        print("Output: ", city_name)
        complete_url = base_url + "q=" + city_name + "&appid=" + api_key
        try:
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["weather"]
                print(y[0]["description"])
                speak(y[0]["description"])
        except Exception as e:
            print("Error: ",e)
            speak("Failed to get")

    if("exit" or "bye" in sentence):
    	print("Meet you soon")

while(1):        
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try: 
            print("Say Something")
            speak("Say Something")
            #r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout = 1)
        except Exception as e:
            print("Error: ", e)
            audio = ""
    try:
        output = r.recognize_google(audio)
        output = output.lower()
    except Exception as e:
        print("Error: ", e)
        output = ""
    print("Output: ", output)
    if "facebook" in output:
        i = 0
        while(i < 5):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                try: 
                    print("How can I help you sir")
                    speak("How can I help you sir")
                    #r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, timeout = 1)
                except Exception as e:
                    print("Error: ", e)
                    audio = ""
            try: 
                data = r.recognize_google(audio)
                data = data.lower()
            except Exception as e:
                print("Error: ", e)
                data = ""
            check_for_greeting(data, i)
            print("Data: ", data)
            i = i + 1
            time.sleep(1)
