import json

with open('Apps-Registered.json', 'r') as fp:
    Sites = json.load(fp)
with open('Sites-Registed.json', 'r') as wp:
    Apps =  json.load(wp)


while True: 
   
    print("Sites registered:")
    print(Sites )
    print()
    print("Apps registered")
    print(Apps )
    print()
    print("to add an app, press a \nto add a website, press w\nto save the registered apps and sites, press s(don't forget) \nto quit, press q\nto delete an app/site, please edit in the json files")
    print()
    x = input()
    if x == "w":
        print("Please tell us your site name")
        sitename = input()
        print("Please tell us your site URL")
        siteURL = input()
        Sites[sitename] = siteURL
    if x =="a": 
        print("Please tell us your app name")
        appname = input()
        print("Please tell us your app path(Ex C:\\Users\\app.exe)")
        appPath = input()
        Apps[appname] = appPath
    
    if x =="s":
        with open('Apps-Registered.json', 'w') as fp:
            json.dump(Apps, fp)
        with open('Sites-Registed.json', 'w') as wp:
            json.dump(Sites, wp)
    


    if x == "q":
        break
    print()