from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Twitter:
    def __init__(self,username,password):
        self.browser =webdriver.Chrome()
        self.username=username
        self.password=password

    def sign(self):
        self.browser.get("https://twitter.com/login")
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input''').send_keys(self.username)
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input''').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input''').send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        followers=[]
        self.browser.get("https://twitter.com/"+self.username)
        time.sleep(1)
        followersRate=self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div[2]/a/span[1]/span''').get_attribute("innerHTML")
        
        self.browser.get("https://twitter.com/"+self.username+"/followers")
        time.sleep(2)
        action =webdriver.ActionChains(self.browser)
        print(followersRate)
        while True:
            for i in range(30):
                try:
                    f=self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div['''+str(i+1)+''']/div/div/div/div[2]/div/div[1]/a''').get_attribute("href").split("/")
                    if f[-1] not in followers:
                        followers.append(f[-1])
                except Exception:
                    pass
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1.5)
            print(str(len(followers))+"--"+str(followersRate))
            if str(len(followers))==str(followersRate):
                break
        

        return followers

    def getFollowing(self):
        following=[]
        self.browser.get("https://twitter.com/"+self.username)
        time.sleep(1)
        followingRate=self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[4]/div[1]/a/span[1]/span''').get_attribute("innerHTML")
        

        self.browser.get("https://twitter.com/"+self.username+"/following")
        time.sleep(2)
        action =webdriver.ActionChains(self.browser)
        print(followingRate)
        while True:
            for i in range(30):
                try:
                    f=self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div['''+str(i+1)+''']/div/div/div/div[2]/div/div[1]/a''').get_attribute("href").split("/")
                    if f[-1] not in following:
                        following.append(f[-1])
                except Exception:
                    pass
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1.5)
            print(str(len(following))+"--"+str(followingRate))
            if str(len(following))==str(followingRate):
                break
        
        return following

    def showUnfollowers(self):
        fing=self.getFollowing()
        time.sleep(2)
        fers=self.getFollowers()
        time.sleep(1)
        print("UNFOLLOWERS LIST")
        for i in fing:
            if i not in fers:
                print(i)

    def closeBrowser(self):
        self.browser.close()

    def searchTweetAbout(self, kelime):
        self.browser.get("https://twitter.com/home")
        time.sleep(2)
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input''').send_keys(kelime)
        time.sleep(1)
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input''').send_keys(Keys.ENTER)
        time.sleep(3)
        action =webdriver.ActionChains(self.browser)
        
        for i in range(10):
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)

        liste=self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]/div[1]")
        
        for i in liste:
            print("\n*************\n")
            print(i.text)
        


me=Twitter(username,password)
me.sign()
