import os
import datetime 
import speech_recognition as sr
from os import path
import pyttsx3
engine = pyttsx3.init()

r = sr.Recognizer()

# initialization

running = True
while running:
    sayStr = ""
    with sr.Microphone() as source:
    
        try:
            print("Say something!")
            audio = r.listen(source)
            print("audio detected")
        except Exception as e :
            print("error: "+str(e))
        
    text = r.recognize_google(audio)
    print(text)
    if("what" in text):
        now = datetime.now()
        if("time" in text):
            sayStr += str(now.strftime("%H:%M "))
        if("day" in text or "date" in text):
            sayStr += str(now.strftime("%B %d, %Y "))
            
        engine.say(sayStr)
    engine.runAndWait()
        
