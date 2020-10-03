from selenium import webdriver
import os 

class Operator:
    SiteNames = []
    Websites = []
    AppName = []
    Apps = []
    OpenedSites = []

    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=C:\\Users\\Andrew Cao\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") #Path to your chrome profile
    driver = webdriver.Chrome('C:\\Users\\Andrew Cao\\Documents\\GitHub\\Personal-laptop-voice-assitance-using-Python\chromedriver\chromedriver.exe',chrome_options=options)

    #add website to list
    def addWebsite(self, sitename, site):
        self.Websites.append(site)
        self.SiteNames.append(sitename)
    
    #add apps to list 
    def addApp(self, appname, app):
        self.Apps.append(app)
        self.AppName.append(appname)
    
    #open the app
    def Open(self, name):

        if name in self.SiteNames:
            self.OpenedSites.append(name)
            openSite = self.Websites[self.SiteNames.index(name)]
            self.driver.execute_script('window.open("{}","_blank");'.format(openSite))

Operator = Operator() 

Operator.addWebsite("Facebook", "https://www.facebook.com")
Operator.Open("Facebook")
    