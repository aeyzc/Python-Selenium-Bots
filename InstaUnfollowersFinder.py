from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Insta:

    def __init__(self, username, password):
        self.browser =webdriver.Chrome()
        self.username=username
        self.password=password

    def sign(self):
        self.browser.get("https://instagram.com/accounts/login")
        time.sleep(3)

        self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input''').send_keys(self.username)
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input''').send_keys(self.password)
        time.sleep(1)
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input''').send_keys(Keys.ENTER)
        time.sleep(3)

    def getFollowers(self):
        self.browser.get(f"https://instagram.com/{self.username}")
        time.sleep(1)
        followersRate=self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span''').get_attribute("title")
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a''').click()
        time.sleep(2)
        dialog=self.browser.find_element_by_xpath("//div[@role='dialog']")
        fcount=len(dialog.find_elements_by_css_selector("li"))
        
        action =webdriver.ActionChains(self.browser)

        #for scrolling
        while True:
            self.browser.find_element_by_xpath('''/html/body/div[4]/div/div[2]/ul/div/li[1]/div''').click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

            time.sleep(0.5)            

            fcount=len(dialog.find_elements_by_css_selector("li"))

            if str(fcount)==followersRate:
                break

        
        followersList=[]

        followers=dialog.find_elements_by_css_selector("li")

        for user in followers:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            link=link.split("/")
            followersList.append(link[-2])

        return followersList

    def getFollowing(self):
        self.browser.get(f"https://instagram.com/{self.username}")
        time.sleep(1)
        followingRate=self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span''').get_attribute("innerHTML")
        self.browser.find_element_by_xpath('''//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a''').click()
        time.sleep(2)
        dialog=self.browser.find_element_by_xpath("/html/body/div[4]/div")
        fcount=len(dialog.find_elements_by_css_selector("li"))
        
        action =webdriver.ActionChains(self.browser)
        
        #for scrolling
        while True:
            self.browser.find_element_by_xpath('''/html/body/div[4]/div/div[2]/ul/div/li[1]/div''').click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

            time.sleep(0.5)            

            fcount=len(dialog.find_elements_by_css_selector("li"))

            if str(fcount)==followingRate:
                break

        
        followingList=[]

        following=dialog.find_elements_by_css_selector("li")

        for user in following:
            link=user.find_element_by_css_selector("a").get_attribute("href")
            link=link.split("/")
            followingList.append(link[-2])

        return followingList
    
    def closeBrowser(self):
        self.browser.close()

    def showUnfollowers(self):
        mFollowing=self.getFollowing()
        mFollowers=self.getFollowers()
        print("\nUNFOLLOWERS LIST")
        for i in mFollowing:
            if i not in mFollowers:
                print(i)

usern=input("Username:")
pw=input("Password:")

me=Insta(usern,pw)
me.sign()
me.showUnfollowers()
me.closeBrowser()