# Logix

## Introduction 

 **Logix** is a program that listens to your voice commands and opens/closes/manipulates applications on your laptop. Inspired by Siri, I wanted to make something that could accelerate and modernize my working space. At the same time, I wanted to explore webscraping for future implementation. This project is also a part of my participation in VandyHacks Hackathon, a Hackathon orgized by my Vanderbilt University. 

## Technologies 

 1. Python 3
 2. Webscraping 
 3. Voice recognition 

## Install 

 The project requires Python 3+ with Selenium, speech_recognition, pyttsx3 installed 

 ```
git clone https://github.com/acao2002/Personal-laptop-voice-assitance-using-Python.git

 ``` 
## Launch 

1. Edit applications/websites that you want to automate
- run this command in the **MainProject-Logix** folder

```
python RegisterApplication.py
```
- Then follow the said instructions 

After you have registered your applications/ website, launch the main application in the **MainProject-Logix** folder

```
python LogixMain.py
```
Now you can open/close applications or chrome tabs by using voice commands. Simple commands like "open facebook" or "close email" should work. 

## More documentation 

To learn more about the project, you can also view my [submission on devpost](https://devpost.com/software/personal-laptop-voice-assitance-using-python) for the VandyHack Hackation

## License 

MIT
