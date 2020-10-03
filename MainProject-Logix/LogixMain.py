import tkinter as tk
from selenium import webdriver
import os 
import speech_recognition as sr
import json

program = False


def Run():
    global program
    if program != True:
        program = True
        slogan.configure(bg="red",text = "STOP")
        LogixSt.configure(text = "Logix is listening", fg = "blue")
    else:
        program = False
        slogan.configure(bg="white",text = "RUN")
        LogixSt.configure(text = "Logix is sleeping", fg = "black")
    
    print(program)
    return program

root = tk.Tk(className = 'My bot')
frame = tk.Frame(root)
frame.pack()
root.geometry("500x200")

slogan = tk.Button(frame,
                   text="RUN" ,
                   bg = "white" ,
                   height = 4,
                   width = 20,
                   command=Run)
slogan.pack(side=tk.TOP)

button = tk.Button(frame, 
                   text="QUIT", 
                   height = 4, 
                   width = 20,
                   fg="red",
                   command=quit)
button.pack(side=tk.TOP)

LogixSt = tk.Label(frame,
                   text = "Logix is sleeping",
                   height = 7,
                   width =40,
                   pady =20)
LogixSt.pack(side=tk.BOTTOM)

root.mainloop()
