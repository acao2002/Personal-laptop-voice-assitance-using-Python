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

## Building Process

To build this app, I have to learn to incorporate different web scraping libraries with Google voice recognition and a text-to-speech engine.

The first part of the app is a platform for users to input the apps/sites that they want Logix to understand. I made this so that Logix can be personalized for different people with different purposes. The inputs are saved in 2 json files which are loaded into the Operator's list of available apps and sites

There's a voiceAi class that utilizes Google's voice recognition library. The class has 2 functions - Listen and Recognize - to listen and output the words spoken by the user.

An Operator class that utilizes selenium and os libraries to close and open applications. It has an Open and Close function incorporated in a Run(method, name) function which passes the method(close or open) and name(app or site) parameter to perform the action.

Finally, the classes are put together in our main program along with pyttsx3 text-to-speech engine to respond to the user depending on whether they ran a task successfully or when errors occur( voice could not be recognized/understood, etc. )

## More documentation 

To learn more about the project, you can also view my [submission on devpost](https://devpost.com/software/personal-laptop-voice-assitance-using-python) for the VandyHack Hackation

## License 

MIT
