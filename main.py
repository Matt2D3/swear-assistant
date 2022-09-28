import os

from datetime import date
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
    
       
        print("Say something!")
        audio = r.listen(source)
        print("audio detected")
        
    text = r.recognize_google(audio)
    if("what" in text):
        now = date.datetime.now()
        if("time" in text):
            sayStr += now.strftime("%H:%M ")
        if("day" in text or "date" in text):
            sayStr += str(today.strftime("%B %d, %Y "))
            
        engine.say(sayStr)
    engine.runAndWait()
        
