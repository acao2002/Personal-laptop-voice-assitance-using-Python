import json

with open('Apps-Registered.json', 'r') as fp:
    Apps = json.load(fp)
with open('Sites-Registed.json', 'r') as wp:
    Sites =  json.load(wp)




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
        S = {}
        print("Please tell us your site name")
        sitename = input()
        print("Please tell us your site URL")
        siteURL = input()
        S['name'] = sitename
        S['url'] = siteURL
        Sites.append(S)
    if x =="a": 
        A = {}
        print("Please tell us your app name")
        appname = input()
        print("Please tell us your app path(Ex C:\\Users\\app.exe)")
        appPath = input()
        A['name'] = appname
        A['path'] = appPath
        Apps.append(A)
    
    if x =="s":
        with open('Apps-Registered.json', 'w') as fp:
            json.dump(Apps, fp)
        with open('Sites-Registed.json', 'w') as wp:
            json.dump(Sites, wp)
    


    if x == "q":
        break
    print()