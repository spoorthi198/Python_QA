from selenium import  webdriver
from selenium.webdriver.chrome.service import Service


s = Service("D:\\drivers\\chromedriver_win32\\chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.google.com/")
mypagetitle = driver.title
print(mypagetitle)
driver.quit()