from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from print import print_, print_find
import time
import random
import pyautogui


class Instabot:

    def __init__(self, username, password, id_taraf):
        self.username = username
        self.password = password
        self.id_taraf = id_taraf
        self.driver = webdriver.Chrome()

    def _verification_code(self):
        sms = input("\n-SMS Verification Code(please check your phone) = ")
        smsf = self.driver.find_element_by_xpath("//input"
                                                 "[@name='verificationCode']")
        smsf.send_keys(sms)
        time.sleep(random.randint(2, 3))
        self.driver.find_element_by_xpath("//button[@type='button']").click()
        # Save pass or not now
        time.sleep(random.randint(8, 10))
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/" 
                                          "main/div/div/div/div/button").click()

    def login(self):
        # The desired page
        self.driver.get("https://www.instagram.com/{}/".format(self.id_taraf))
        time.sleep(random.randint(2, 5))
        # agar error dar vorod etelat shdo in ra comment kon
        # bayad ye if barash dorost konam khodesh tashkhis  bede
        # self.driver.find_element_by_xpath("//button[@type='button']").click()
        user_name = self.driver.find_element_by_xpath("//input"
                                                      "[@name='username']")
        pass_word = self.driver.find_element_by_xpath("//input"
                                                      "[@name='password']")
        time.sleep(random.randint(2, 4))
        if user_name and pass_word:
            user_name.send_keys(self.username)
            time.sleep(random.randint(2, 5))
            pass_word.send_keys(self.password + Keys.ENTER)
        else:
            self.driver.find_element_by_xpath("//button[@type='button']").click()
            user_name.send_keys(self.username)
            time.sleep(random.randint(2, 5))
            pass_word.send_keys(self.password + Keys.ENTER)
        # Ask for sms verification
        time.sleep(random.randint(5, 6))
        if ask == "y":
            self._verification_code()

    def following_section(self):
        time.sleep(4)
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/"
        #                                   "div[1]/div/div/div[1]/div[1]/"
        #                                   "section/main/div/header/section/"
        #                                   "ul/li[3]/a/div").click()
        self.driver.find_element_by_xpath("//a[contains(@href, "
                                           "'/following')]").click()
        scrol_aval1_dovom2 = 1  # tozih dar paein bakhshe _get_names()
        following = self._get_names(scrol_aval1_dovom2)  # chon scrol following ba follower fargh dare (xpath) an
        return following

    def followers_section(self):
        time.sleep(4)
        # self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/"
        #                                   "div[1]/div/div/div[1]/div[1]/"
        #                                   "section/main/div/header/"
        #                                   "section/ul/li[2]/a/div").click()
        self.driver.find_element_by_xpath("//a[contains(@href,"
                                           " '/followers')]").click()
        time.sleep(random.randint(5, 7))
        scrol_aval1_dovom2 = 2
        followers = self._get_names(scrol_aval1_dovom2)
        return followers

    # def print_find(self, not_following_back):
    #     print("\n\nThese people did not follow this page({}):".format(
    #         self.id_taraf))
    #     for a in not_following_back:
    #         print("----->  " + a)

    def find(self):
        # This part find who unfollowed you
        print("\n\n-Please wait a moment...\n")
        following = self.following_section()
        followers = self.followers_section()
        # bakhshe peyda kardan
        not_following_back = [user for user in following if user not in followers]
        #self.print_find(not_following_back)
        return not_following_back

    # scrol and get page id
    def _get_names(self, scrol_box_tedad):
        # scrol_following = "//*[@id='mount_0_0_zp']/div/div[1]/div/" \
        #                   "div[2]/div/div/div[1]/div/div[2]/div/" \
        #                   "div/div/div/div/div/div/div[3]"
        # scrol_followers = "//*[@id='mount_0_0_zp']/div/div[1]/div/" \
        #                   "div[2]/div/div/div[1]/div/div[2]/div/" \
        #                   "div/div/div/div/div/div/div[2]"
        # clos_box = "//*[@id='mount_0_0_Xt']/div/div[1]/div/div[2]/div/" \
        #                                  "div/div[1]/div/div[2]/div/div/" \
        #                                  "div/div/div/div/div/div[1]/div/" \
        #                                  "div[3]/div/button"
        time.sleep(random.randint(3, 5))
        # morabae follow va following
        # scro_aval... : in bakhsh baraye ine ke XPATH scroll box bakhsh following va followers fargh darad.agar 1 bashad yani following va agar 2 bashad yani follower
        # if scrol_box_tedad == 1:
        #     # scroll_box = self.driver.find_element_by_xpath(scrol_following)
        #     scroll_box = self.driver.find_element_by_xpath("//div"
        #                                                    "[@class='_aano']")
        # elif scrol_box_tedad == 2:
        #     # scroll_box = self.driver.find_element_by_xpath(scrol_followers)
        #     scroll_box = self.driver.find_element_by_xpath("//div"
        #                                                    "[@class='_aano']")
        scroll_box = self.driver.find_element_by_xpath("//div"
                                                       "[@class='_aano']")

        time.sleep(random.randint(5, 7))
        # height variable
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(random.randint(2, 3))
            # scroll down and retrun the height of scroll (JS script)
            ht = self.driver.execute_script(""" 
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight; """, scroll_box)

        time.sleep(random.randint(3, 5))
        print("\n\n-Please wait a moment...\n")
        # links = scroll_box.find_elements_by_tag_name("a")
        links = scroll_box.find_elements_by_tag_name("a")
        time.sleep(random.randint(2, 3))
        names = [name.text for name in links if name.text != '']
        # zarbdar   ke az Esc estefade mikonim
        time.sleep(2)
        pyautogui.press('esc')
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
    find_follow = test.find()
    print_find(find_follow, test.id_taraf)
