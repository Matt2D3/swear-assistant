import os
import datetime 
import speech_recognition as sr
from os import path
import pyttsx3
engine = pyttsx3.init()

r = sr.Recognizer()

running = True
while running:
    sayStr = ""
    text = ""
    with sr.Microphone() as source:   
        try:
            print("Say something!")
            audio = r.listen(source)
            print("audio detected")
            text = r.recognize_google(audio).lower()
        except Exception as e :
            print("error: "+str(e))    
            text = ""
    print(text)
    if("what" in text):
        now = datetime.now()
        if("time" in text):
            sayStr += str(now.strftime("%H:%M "))
        if("day" in text or "date" in text):
            sayStr += str(now.strftime("%B %d, %Y "))   
    if("look up" in text or "search for" in text or "on google"):
        
        if("on google" in text):

            after_keyword = text
            if("look up" in text):
                before_keyword, keyword, after_keyword = text.partition("look up ")
            if("search for" in text.lower()):
                before_keyword, keyword, after_keyword = text.partition("search for ")
            after_keyword = after_keyword.replace(" on google" , "")
            after_keyword = after_keyword.replace(" ","+")
            command = (str("firefox https://www.google.com/search?q="+after_keyword))
            print(after_keyword)
            print(command)
            
            os.system(command)
        if("on youtube" in text):

            after_keyword = text
            if("look up" in text):
                before_keyword, keyword, after_keyword = text.partition("look up ")
            if("search for" in text):
                before_keyword, keyword, after_keyword = text.partition("search for ")  
            after_keyword = after_keyword.replace(" on youtube" , "")
            after_keyword = after_keyword.replace(" ","+")
            command = (str("firefox https://www.youtube.com/results?search_query="+after_keyword))
            print(after_keyword)
            print(command)
            
            os.system(command)
            command = ""
    if(sayStr != ""):  
        engine.say(sayStr)
        engine.runAndWait()
