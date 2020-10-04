from selenium import webdriver
import os 
import speech_recognition as sr
import json
from OperatorClass import Operator 
from VoiceInputClass import VoiceAI 
import pyttsx3

engine = pyttsx3.init()

with open('Apps-Registered.json', 'r') as fp:
    Apps = json.load(fp)
with open('Sites-Registed.json', 'r') as wp:
    Sites =  json.load(wp)

Operator = Operator()

for item in Apps:
    Operator.AppNames.append(item['name'])
    Operator.Apps.append(item['path'])
    


for item in Sites:
    Operator.SiteNames.append(item['name'])
    Operator.Websites.append(item['url'])

VoiceAI = VoiceAI()

def returnMethod(string):
    for item in string:
        if item == "open" or item =="close":
            return item 
        

def returnName(string):
    for s in string:
        for a in (Operator.SiteNames+Operator.AppNames):
            if s == a:
                return s

logixorder = 0          
while True:
    if logixorder == 0:
        engine.say("Hi I am Logix, How can I help you")
        engine.runAndWait()
    elif logixorder == 2:
        engine.say("Please repeat your order")
        engine.runAndWait()
    else: 
        engine.say("How else can I help you")
        engine.runAndWait()
    VoiceAI.Listen()
    Command = str(VoiceAI.Recognize()).lower().split()
    method = returnMethod(Command)
    name = returnName(Command)

    print(method, name)
   
    if method != None and name != None:
        engine.say("Task completed")
        engine.runAndWait()
        logixorder = 1
    else:
        engine.say("I could not understand you sir")
        engine.runAndWait()
        logixorder = 2
    
    Operator.Run(method, name)
