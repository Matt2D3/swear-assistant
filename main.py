import os
import wikipedia 
from datetime import datetime 
import speech_recognition as sr
from os import path
import pyttsx3
engine = pyttsx3.init()

engine.setProperty('rate', 150)
print("by the way I use linux")
engine.say("by the way I use linux")
engine.runAndWait()
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
r = sr.Recognizer()
devMode = False
running = True
if(devMode == False):
    m = sr.Microphone() 
    with m as source:
        r.adjust_for_ambient_noise(source)
while running:
    sayStr = ""
    text = ""
    if(devMode == False):
        with sr.Microphone() as source:   
            try:
                print("Say something!")
                r.pause_threshold = 1
                audio = r.listen(source)
                print("audio detected")
                text = r.recognize_google(audio).lower()
            except Exception as e :
                print("error: "+str(e))    
                text = ""
            print(text)
    if(devMode == True):
        text = input("command: ")
    
    if("what" in text):
        if("drawing" in text): # tech drawing
            sayStr += "in technical drawing, we learn to design and build architecture and engineering projects and activities which include: sketching, drawing, cad, 3D printing, laser engraving, model building, and graphics. this smart speaker is a project for tech drawing. "
        if("drone" in text): # drone tech
            sayStr += "in drone tech, you learn how to fly a drone, how to take good photos with drones, and how to take cinimatic videos with drones. along with the laws regarding how, what, when, and where you can fly. "
        if("graphics" in text): # computer graphics 
            sayStr += "in computer graphics, students will explore the amazing visual potential in computer genorated graphics. "
        if("electronics" in text or "robotics" in text): # electronics and robotics
            sayStr += "in electronics and robotics class, you learn the basics on how to build and program a robot, aswell as compete in a class competition where you build and drive your own robot to compete against other robots. "
            sayStr += "you also learn the basics of how electrical circuts work and the math used to design them. "
        if("home" in text or "know your" in text): # know your home 
            sayStr += "know your home is where you learn about home repair and construction technology to solve practical problems found in the home. "
        if("squad" in text): # design squad
            sayStr += "in design squad, use the design process to solve an engineering problem. "
        now = datetime.now().time()
        if("time" in text):
            sayStr += str(now.strftime("%H:%M "))
        if("day" in text or "date" in text):
            sayStr += str(now.strftime("%B %d, %Y "))  
    if("look up" in text or "search for" in text):
        if("on wikipedia" in text):
            if("look up" in text):
                before_keyword, keyword, after_keyword = text.partition("look up ")
            if("search for" in text):
                before_keyword, keyword, after_keyword = text.partition("search for ")
            try:
                sayStr += wikipedia.summary(after_keyword, sentences=1)
            except:
                sayStr+= ("I couldn't find that topic on wikipedia, which is impressive. good job")
    if(sayStr != ""):  
        print(sayStr)
        engine.say(sayStr)
        engine.runAndWait()