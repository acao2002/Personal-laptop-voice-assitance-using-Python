from selenium import webdriver
import os 

class Operator:
    SiteNames = []
    Websites = []
    AppNames = []
    Apps = []
    OpenedSites = ["newtab"]

    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=C:\\Users\\Andrew Cao\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
     #Path to your chrome profile
    

    #add website to list
    def addWebsite(self, sitename, site):
        self.Websites.append(site)
        self.SiteNames.append(sitename)
    
    #add apps to list 
    def addApp(self, appname, path):
        self.Apps.append(path)
        self.AppNames.append(appname)
    
    #open the app
    def Open(self, name):

        if name in self.SiteNames:
            if len(self.OpenedSites) == 1:
                self.driver = webdriver.Chrome('C:\\Users\\Andrew Cao\\Documents\\GitHub\\Personal-laptop-voice-assitance-using-Python\chromedriver\chromedriver.exe',chrome_options=self.options)
            self.OpenedSites.append(name)
            openSite = self.Websites[self.SiteNames.index(name)]
            self.driver.execute_script('window.open("{}","_blank");'.format(openSite))
        
        elif name in self.AppNames:
             os.startfile(self.Apps[self.AppNames.index(name)])
    
    def Close(self, name):

        if name in self.OpenedSites:
            self.driver.switch_to_window(self.driver.window_handles[self.OpenedSites.index(name)])
            self.OpenedSites.remove(name)
            self.driver.close()
        
        else: 
             os.system('TASKKILL /F /IM ' + name +'.exe')

    def Run(self, method, name):

        if method == "open":
            self.Open(name)
        if method == "close":
            self.Close(name)

'''
Operator = Operator()

Operator.addApp('audacity','C:\\Program Files (x86)\\Audacity\\audacity.exe')
Operator.Run('open','audacity')

Operator.addWebsite("facebook", "https://www.facebook.com")
Operator.addWebsite("email", "https://www.gmail.com")
Operator.Run('open',"facebook")
Operator.Run('close',"facebook")
Operator.Run('close',"audacity")
print (Operator.OpenedSites)
'''

