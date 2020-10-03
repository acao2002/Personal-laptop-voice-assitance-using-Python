import os 
while True: 
    print("what do you want?")
    a = input()
    if a == "open":
        os.startfile('C:\\Program Files (x86)\\Audacity\\audacity.exe')
    else: 
        os.system('TASKKILL /F /IM '+'audacity'+'.exe')
