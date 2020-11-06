# Imports
from selenium import webdriver
import bs4 as bs
import time
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

# Replacing the login.passwords with the personal ProtonMail Account
mailAccount = "";
passwordAccount = "";

# Opening the file and reading the login and password to the declared variable
with open("login.passwords", "r") as loginpass:
    theUserInput = loginpass.read().split(";")
    mailAccount = theUserInput[0]
    passwordAccount = theUserInput[1]

# Reading the chromedriver path
option = webdriver.ChromeOptions()
option.add_argument('headless')

browser = webdriver.Chrome("C:\Program Files\chromedriver\chromedriver.exe", options=option)

# Opening the website
url = "https://protonmail.com/login"
browser.get(url)

time.sleep(1)

# Login field Xpath Declaration and inputting the mail
protonMailLoginInput = browser.find_element_by_xpath("//*[@id='username']")
protonMailLoginInput.send_keys(mailAccount)

# Password field Xpath Declaration and inputting the password
protonMailPasswordInput = browser.find_element_by_xpath("//*[@id='password']")
protonMailPasswordInput.send_keys(passwordAccount)

# Entering the mail account
protonMailLoginButton = browser.find_element_by_xpath("//*[@id='login_btn']")
protonMailLoginButton.click()

time.sleep(4)

# Update Mail Button
updateMailButton = browser.find_element_by_xpath("//*[@id='pm_sidebar']/ul[1]/li[8]/a")

# Moving to the All Mail Section
updateMailButton.click()
time.sleep(1)

# Latest Mail Title
latestMailPath = browser.find_element_by_xpath("//*[@id='conversation-list-columns']/section/div[1]/div[2]/div[1]/h4/span[2]").text
#print(latestMailPath)

# Mail Time Xpath
mailTimeX = browser.find_element_by_xpath("//*[@id='conversation-list-columns']/section/div[1]/div[2]/div[1]/span/time").text

ddosAndTime = []
print("GOT A NEW MAIL!")
ddosAndTime.append(mailTimeX)
print(ddosAndTime)

# Mail sender name:
mailSenderNameX = browser.find_element_by_xpath("//*[@id='conversation-list-columns']/section/div[1]/div[2]/div[2]/span/span").text
                                                #//*[@id="conversation-list-columns"]/section/div[1]/div[2]/div[2]/span/span
print(mailSenderNameX)
mailSendersName = []
mailSendersName.append(mailSenderNameX)
#print(mailSenderNameX)

while True:
    updateMailButton.click()
    time.sleep(1)

    latestMailPath = browser.find_element_by_xpath("//*[@id='conversation-list-columns']/section/div[1]/div[2]/div[1]/h4/span[2]").text
    if latestMailPath.lower() == "ddos":
        mailTimeX = browser.find_element_by_xpath("//*[@id='conversation-list-columns']/section/div[1]/div[2]/div[1]/span/time").text
        mailSenderNameX = browser.find_element_by_xpath("//*[@id='conversation-list-columns']/section/div[1]/div[2]/div[2]/span/span").text
                                                        #//*[@id="conversation-list-columns"]/section/div[1]/div[2]/div[2]/span/span

        time.sleep(0.5)
        if mailTimeX not in ddosAndTime:
            print("DDOSed! FAST FAST RECOVER UR ASS!")
            ddosAndTime.append(mailTimeX)
            mailSendersName.append(mailSenderNameX)

    print("DDOS included mail was sent at ", ddosAndTime)
    print("Mail was sent by ", mailSendersName)

    #print(latestMailPath)
    time.sleep(3)
