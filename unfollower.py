from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("""
               __      _ _                        
  instagram   / _|    | | |                       
  _   _ _ __ | |_ ___ | | | _____      _____ _ __ 
 | | | | '_ \|  _/ _ \| | |/ _ \ \ /\ / / _ \ '__|
 | |_| | | | | || (_) | | | (_) \ V  V /  __/ |   
  \__,_|_| |_|_| \___/|_|_|\___/ \_/\_/ \___|_| by Novin.Nouri

Part of it,I got help from <Lazar Gugleta's> content.
""")
class Instabot():
    
    def __init__(self,username,password,id_taraf):
        self.username = username
        self.password = password
        self.id_taraf = id_taraf
        self.driver = webdriver.Chrome()

    def login(self):
        #The desired page
        self.driver.get("https://www.instagram.com/{}/".format(self.id_taraf))
        #login
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@type='button']").click()
        user_name = self.driver.find_element_by_xpath("//input[@name='username']")
        user_name.send_keys(self.username)
        pass_word = self.driver.find_element_by_xpath("//input[@name='password']")
        pass_word.send_keys(self.password + Keys.ENTER)
        #ask & sms verification
        time.sleep(5)
        if ask == "y": 
            sms = input("\n-SMS Verification Code(please check your phone) = ")
            smsf = self.driver.find_element_by_xpath("//input[@name='verificationCode']") 
            smsf.send_keys(sms)
            self.driver.find_element_by_xpath("//button[@type='button']").click()
      
    def follow(self):
        print("\n\n-Please wait a moment...\n")
        #following 
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        following = self._get_names()
        #follower
        time.sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        followers = self._get_names()
        #find 
        not_following_back = [user for user in following if user not in followers]
        #print(not_following_back)
        print("\n\nThese people did not follow this page({}):".format(self.id_taraf))
        for a in not_following_back:
            print("----->  " + a) 

    #scrol and get page id
    def _get_names(self):
        time.sleep(2)
        #scroll_box and find tag name("a")
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht,ht = 0,1
        while last_ht != ht:
            last_ht = ht
            time.sleep(2)
            ht = self.driver.execute_script("""
                   arguments[0].scrollTo(0,arguments[0].scrollHeight);
                   return arguments[0].scrollHeight;
                   """,scroll_box)
        links = scroll_box.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != '']
        #close scroll_box
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names
          
    def quit(self):
        self.driver.quit()

user8 = "your username"
pass8 = "your password"
id8 = input("-The desired page = ")         
ask = input("-Did you enable verification Code?[y/n] ")
test = Instabot(user8,pass8,id8)
#Run \|/
test.login()
test.follow()
