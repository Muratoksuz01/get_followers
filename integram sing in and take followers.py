import chromedriver_autoinstaller as chromedriver
chromedriver.install()
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class Integram():
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.browser=webdriver.Chrome()
    def sing_in(self):
        url="https://www.instagram.com/accounts/login/?next=/login/"
        self.browser.get(url)
        sleep(1)
        self.browser.find_element("name","username").send_keys(self.username)
        self.browser.find_element("name","password").send_keys(self.password)
        sleep(1)
        self.browser.find_element("xpath","//*[@id='loginForm']/div/div[3]/button").click()
        sleep(3)
    def getfollowing(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        sleep(4)
        self.browser.find_element("xpath","//html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div").click() 
        sleep(3)
        self.scroolDown()
        takipciler=self.browser.find_elements(By.CLASS_NAME,"_ab8w._ab94._ab97._ab9f._ab9k._ab9p._ab9-._aba8._abcm") 
        say=1
        for takipci in takipciler:
            name=takipci.find_element(By.CLASS_NAME,"_ab8y._ab94._ab97._ab9f._ab9k._ab9p._abcm")
            takipci_link="https://www.instagram.com/"+name.text
            print(str(say)+"-->"+name.text +"-->"+takipci_link)
            say+=1
    def scroolDown (self):
        jsKomut = """
            sayfa = document.querySelector("._aano");
            sayfa.scrollTo(0, sayfa.scrollHeight);
            var sayfaSonu = sayfa.scrollHeight;
            return sayfaSonu;"""

        sayfaSonu = self.browser.execute_script (jsKomut)
        while True:
            son=sayfaSonu
            sleep(1)
            sayfaSonu=self.browser.execute_script(jsKomut)
            if son==sayfaSonu:
                break


            
username=input("please into your username:")
password=input("please into your password:")
inte=Integram(username,password)
inte.sing_in()
inte.getfollowing()