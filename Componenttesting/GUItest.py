import tkinter as tk

a = False


def Run():
    global a
    if a != True:
        a = True
        slogan.configure(bg="red",text = "STOP")
    else:
        a = False
        slogan.configure(bg="white",text = "RUN")
    
    print(a)
    return a

root = tk.Tk(className = 'My bot')
frame = tk.Frame(root)
frame.pack()
root.geometry("500x200")

slogan = tk.Button(frame,
                   text="RUN" ,
                   bg = "white" ,
                   height = 5,
                   width = 20,
                   command=Run)
slogan.pack(side=tk.LEFT)

button = tk.Button(frame, 
                   text="QUIT", 
                   height = 5, 
                   width = 20,
                   fg="red",
                   command=quit)
button.pack(side=tk.RIGHT)




root.mainloop()