from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from print import print_


class Instabot:
    
    def __init__(self, username, password, id_taraf):
        self.username = username
        self.password = password
        self.id_taraf = id_taraf
        self.driver = webdriver.Chrome()

    def verification_code(self):
        sms = input("\n-SMS Verification Code(please check your phone) = ")
        smsf = self.driver.find_element_by_xpath(
            "//input[@name='verificationCode']")
        smsf.send_keys(sms)
        self.driver.find_element_by_xpath("//button[@type='button']").click()

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
            self.verification_code()

    def follow(self):
        print("\n\n-Please wait a moment...\n")
        following = self.check_following()
        followers = self.check_follwers()
        #find 
        not_following_back = [user for user in following if user not in followers]
        #print(not_following_back)
        print("\n\nThese people did not follow this page({}):".format(self.id_taraf))
        for a in not_following_back:
            print("----->  " + a) 

    #scrol and get page id

    def check_following(self):
        # following
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        following = self._get_names()
        return following

    def check_follwers(self):
        # follower
        time.sleep(4)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        followers = self._get_names()
        return followers

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


if __name__ == "__main__":
    print_()
    user8 = input("pleas enter your username= ")
    pass8 = input("pleas enter your password= ")
    id8 = input("-The desired page for find those= ")
    ask = input("-Did you enable verification Code?[y/n] ")

    test = Instabot(user8, pass8, id8)
    test.login()
    test.follow()
