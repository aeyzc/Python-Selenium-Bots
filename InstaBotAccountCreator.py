from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

#random names maker
def nameMaker():
    names="jack","margaret","george","maria","nicole","justin","stephanie","candice","alice","robert","jon","richard","melanie"
    surnames="anderson","baker","carter","clarke","cooper","hamilton","lawrence","lewis","miller","martin"
    return random.choice(names).capitalize()+" "+random.choice(surnames).capitalize()

#username maker
def usernameMaker(email):
    a=email.split('@')
    return a[0]

#random email maker
def emailMaker():
    mail=""
    alpha=list(map(chr, range(97, 123)))
    bat=random.randint(4,11) #before @
    aat=random.randint(4,7)  #after @
    for i in range(bat):
        mail=mail+random.choice(alpha)
    mail=mail+"@"
    for i in range(aat):
        mail=mail+random.choice(alpha)
    mail=mail+".com"
    return mail


driver=webdriver.Chrome()
action = ActionChains(driver)

email=emailMaker()
password="aeyzc123"
driver.get("https://www.instagram.com/accounts/emailsignup/?hl=en")
time.sleep(2)

#email
driver.find_element_by_xpath('''/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input''').send_keys(email)

#name
driver.find_element_by_xpath('''/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input''').send_keys(nameMaker())

#username
try:
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/div/div/button/span''').click() #for auto username creator button
except Exception:
    driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input''').send_keys(usernameMaker(email))
time.sleep(2)
username=driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input''').get_attribute("value")

#password
driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input''').send_keys(password)
time.sleep(1)

#button
driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button''').click()
time.sleep(2)

#birthday page
driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select''').click()
action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select''').click()
action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select''').click()
action.key_down(Keys.NUMPAD1).key_up(Keys.NUMPAD1).perform()
action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
time.sleep(1)

#button
driver.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button''').click()

print("ACCOUNT CREATED!\n\nPsername:"+str(username)+"\nPassword:"+str(password))
