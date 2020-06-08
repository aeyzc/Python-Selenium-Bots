#PLEASE CHECK LINE 43 AND LINE 44 BEFORE RUN IT

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Insta:

    def __init__(self, username, password):
        self.browser =webdriver.Chrome()
        self.username=username
        self.password=password

    def sign(self):
        self.browser.get("https://instagram.com/accounts/login")
        time.sleep(3)

        try:
            self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input''').send_keys(self.username)
            self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input''').send_keys(self.password)
            time.sleep(1)
            self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input''').send_keys(Keys.ENTER)
            time.sleep(3)
        #if browser go main page
        except Exception:
            self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input''').send_keys(self.username)
            self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input''').send_keys(self.password)
            time.sleep(1)
            self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input''').send_keys(Keys.ENTER)
            time.sleep(3)


    def followit(self,site):
        self.browser.get("https://www.instagram.com/"+site)
        time.sleep(2)
        self.browser.find_element_by_css_selector('button').click()

    def likeit(self,site):
        self.browser.get(site)
        time.sleep(2)
        self.browser.find_element_by_css_selector('button svg').click()
        
BotUsernames='example1',"example2","example3"       #add here bot accounts usernames
BotPasswords='example1pw',"example2pw","example3pw" #add here bot accounts passwords

print('''  _____           _                                    ____        _   
 |_   _|         | |                                  |  _ \      | |  
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ 
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|
  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | | |_) | (_) | |_ 
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|
                            __/ |                              by aeyzc
                           |___/                                       ''')

select=input("\n1-Follow\n2-Like\n3-Exit")

if select=='1' or select=='2':
    if select=='1':
        site=input("\nusername to follow:")

    else:
        site=input('\nphoto url to like:')

    i=0
    for i in range(len(BotUsernames)):
        bot=Insta(BotUsernames[i],BotPasswords[i])
        bot.sign()
        if select=='1':
            bot.followit(site)
        elif select=='2':
            bot.likeit(site)
        time.sleep(2)
        bot.browser.close()
        i+=1
