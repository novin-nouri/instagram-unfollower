from selenium import webdriver
from selenium.webdriver import Keys
import random
import time
import pyautogui


class Insta:

    def __init__(self, username, password, desired_page, verification):
        self.username = username
        self.password = password
        self.desired_page = desired_page
        self.verification = verification
        self.driver = webdriver.Chrome()

    def __repr__(self):
        return f"{self.__class__.__name__}" \
               f"({self.username!r}, {self.password!r}, " \
               f"{self.desired_page!r}, {self.verification!r})"

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(random.randint(2, 5))
        user_name = self.driver.find_element_by_xpath("//input"
                                                      "[@name='username']")
        user_name.send_keys(self.username)
        time.sleep(random.randint(2, 5))
        pass_word = self.driver.find_element_by_xpath("//input"
                                                      "[@name='password']")
        pass_word.send_keys(self.password + Keys.ENTER)
        time.sleep(random.randint(5, 6))
        # Ask for sms verification(if enable the sms verification)
        if self.verification == "y":
            self._verification_code()
        self._save_pass()
        time.sleep(random.randint(2, 3))
        self.driver.get(f"https://www.instagram.com/{self.desired_page}/")
        time.sleep(random.randint(2, 3))

    def _verification_code(self):
        sms = input("\n-SMS Verification Code(please check your phone) = ")
        smsf = self.driver.find_element_by_xpath("//input"
                                                 "[@name='verificationCode']")
        smsf.send_keys(sms)
        time.sleep(random.randint(2, 3))
        self.driver.find_element_by_xpath("//button[@type='button']").click()

    def _save_pass(self):
        # This functioin close (save pass or not now) box
        time.sleep(random.randint(8, 10))
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/"
                                          "div/div/div/div/button").click()

    def find(self):
        # This part find who unfollowed you
        print("\n\n-Please wait a moment...\n")
        following = self._following_section()
        followers = self._followers_section()
        not_following_back = [user_id for user_id in following if user_id \
                              not in followers]
        return not_following_back

    def _following_section(self):
        # Returns all your following
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href, "
                                          "'/following')]").click()
        following = self._get_names()
        return following

    def _followers_section(self):
        # Returns all your following
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href,"
                                          " '/followers')]").click()
        followers = self._get_names()
        return followers

    def _get_names(self):
        # Get all page id from following and followers box
        time.sleep(random.randint(3, 5))
        scroll_box = self.driver.find_element_by_xpath("//div"
                                                       "[@class='_aano']")
        time.sleep(random.randint(5, 7))
        self._scroll_down(scroll_box)
        time.sleep(random.randint(3, 5))
        print("\n\n-Please wait a moment...\n")
        names = self._separate_names(scroll_box)
        time.sleep(2)
        # Close scrol box
        pyautogui.press('esc')
        return names

    def _scroll_down(self, scroll_box):
        # Scrol down
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(random.randint(2, 3))
            ht = self.driver.execute_script(""" 
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight; """, scroll_box)

    @staticmethod
    def _separate_names(scroll_box):
        # This part shows those who unfollowed your page
        links = scroll_box.find_elements_by_tag_name("a")
        time.sleep(random.randint(2, 3))
        names = [name.text for name in links if name.text != '']
        return names

    def quit(self):
        self.driver.quit()