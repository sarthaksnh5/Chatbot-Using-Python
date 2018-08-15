import random #for random function
import time #for delay if you want
import re #split text
import datetime #current date and time

#q stands for question and a stands for answer like
#ownerq = asking question about owner
#ownera = answer about owner

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "namaste")

GREETING_RESPONSES = ["Yo!", "hey", "hi", "hello",]

moodq = ["happy", "nice", "good", "awesome", "fine"]
moodr = ["Oh! thats very good", "I am also like you", "good thing"]
moods = ["sad", "bad", "very sad","not good"]

ownerq = ["who made you", "who is you owner", "who is your head", "to whom you belong"]
ownera = ["My lord", "My lord is your friend", "Your friend", "He is like you only", "A person like you"]

laughq = ["laugh", "joke"]
laugha = ["Did you hear about the blind carpenter who picked up his hammer and saw?", "A teacher is talking to a student.Teacher: Did your father help you with your homework? Student: No, he did it all by himself.","On a crowded bus, one man noticed that another man had his eyes closed. What's the matter? Are you sick? No, I'm okay. It's just that I hate to see an old lady standing."]

nameq = ["call me","my name is"]

dateq = ["date", "time"]

#for loop will check each and every line for better response

def check_for_greeting(sentence):
    for i in range(0,6):
        if GREETING_KEYWORDS[i] in sentence:
            print(random.choice(GREETING_RESPONSES))
            print("How are you?")
            
    for i in range(0,5):
        if moodq[i] in sentence:
            print(random.choice(moodr), " ", "It would be great to talk with you")
            print("Now, What you want me to do")

    for i in range(0,3):
        if sentence == moods[i]:
            print("Why?"," ","How can I Help?")

    if sentence == "calculator":
        print("Tell me numbers: ")
        a=int(input())
        b=int(input())
        print("Tell me what you want: ", "\r", "1: add", "\r", "2: subtract", "\r", "3: multiply", "\r", "4: divide")
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

    if sentence == "sing a song":
        print("What type of song you want?")
        j=input()
        if "hindi" in j:
            print("You shound go for Saavn.com or Gaana.com")
        elif "punjabi" in j:
            print("You shound go for djpunjab.com or pagaljatt.com")
        elif "english" in j:
            print("You hsould go for google only I am an Indian")
        else:
            print("Search it on google","\r","I know about only english, hindi, punjabi")
    
    for i in range (0,4):
        if sentence == ownerq[i]:
            print(random.choice(ownera))
            print("His Name is: Sarthak")
            print("My lord mail is: sarthaksnh5@gmail.com","\n")
            print("His contact number is: 9056317518","\n")

    for i in range(0,2):
        if laughq[i] in sentence:
            print(random.choice(laugha))

    if nameq[0] in sentence:
        splitted = sentence.split()
        a=splitted[2]
        print(random.choice(GREETING_RESPONSES),a)

    if nameq[1] in sentence:
        splitted=sentence.split()
        a=splitted[3]
        print(random.choice(GREETING_RESPONSES),a)

    for i in range(0,2):
        if dateq[i] in sentence:
            now=datetime.datetime.now()
            print("Current date and time: ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            
#while loop will continue infinite times
while(True):
    
    i=input()
    check_for_greeting(i)

#print("Hello")


