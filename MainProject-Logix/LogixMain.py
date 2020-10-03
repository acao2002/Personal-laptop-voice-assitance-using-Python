from selenium import webdriver
import os 
import speech_recognition as sr
import json
from OperatorClass import Operator 
from VoiceInputClass import VoiceAI 

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
            
while True:
    print("say sth")
    VoiceAI.Listen()
    Command = VoiceAI.Recognize().lower().split()
    method = returnMethod(Command)
    name = returnName(Command)
    print(method, name)
    Operator.Run(method, name)
    

