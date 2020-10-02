from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\Andrew Cao\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1") #Path to your chrome profile
driver = webdriver.Chrome('C:\\Users\\Andrew Cao\\Documents\\GitHub\\Personal-laptop-voice-assitance-using-Python\chromedriver\chromedriver.exe',chrome_options=options)
driver.get('https://www.facebook.com')

driver.execute_script("window.open('https://www.gmail.com');")


