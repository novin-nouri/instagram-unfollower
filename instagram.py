from selenium import webdriver
from selenium.webdriver import Keys
import random
import time
import pyautogui


class Insta:
    """Class to find who unfollowed you"""

    def __init__(self, username, password, desired_page, verification):
        self.username = username
        self.password = password
        self.desired_page = desired_page
        self.verification = verification
        self.driver = webdriver.Chrome()
    """Initializes a Insta
    
    Args:
        username: Your instagram username
        password: Your instagram password
        desired_page: A page username you want to find out who has unfollowed it
        verification: For those who have enable sms verification from setting
    """

    def __repr__(self):
        return f"{self.__class__.__name__!r}({self.__dict__!r})"

    def login(self):
        """Login in your desired page in instagram"""
        # First open instagram
        self.driver.get("https://www.instagram.com/")
        time.sleep(random.randint(2, 5))
        # enter username and password to log in to Instagram
        user_name = self.driver.find_element_by_xpath("//input"
                                                      "[@name='username']")
        user_name.send_keys(self.username)
        time.sleep(random.randint(2, 5))
        pass_word = self.driver.find_element_by_xpath("//input"
                                                      "[@name='password']")
        pass_word.send_keys(self.password + Keys.ENTER)
        # ask for sms verification(if you don't activate sms verification)
        if self.verification == "n":
            # it's now logged in to your account
            time.sleep(random.randint(5, 6))
            self._save_pass()
            time.sleep(random.randint(2, 3))
            # open desired page
            self.driver.get(f"https://www.instagram.com/{self.desired_page}/")
            time.sleep(random.randint(2, 3))

    def verification_code(self):
        """For those who have enable sms verification from setting"""
        time.sleep(random.randint(3, 5))
        with open("smscode.txt", "r") as f:
            sms = f.read()
        # enter sms verification code
        sms_code = self.driver.find_element_by_xpath("//input"
                                                     "[@name="
                                                     "'verificationCode']")
        sms_code.send_keys(sms)
        time.sleep(random.randint(2, 3))
        # click on Confirm button
        self.driver.find_element_by_xpath("//button[@type='button']").click()
        # it's now logged in to your account
        self._save_pass()
        time.sleep(random.randint(2, 3))
        # open desired page
        self.driver.get(f"https://www.instagram.com/{self.desired_page}/")
        time.sleep(random.randint(2, 3))

    def _save_pass(self):
        """This functioin close (save pass or not now) box"""
        time.sleep(random.randint(8, 10))
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/"
                                          "div/div/div/div/button").click()

    def find(self):
        """This part find who unfollowed you

        Return:
            A list of the who unfollowed you
        """
        following = self._following_section()
        followers = self._followers_section()
        # now we know who unfollowed you
        not_following_back = [user_id for user_id in following if user_id \
                              not in followers]
        return not_following_back

    def _following_section(self):
        """Returns all your following

        Returns:
            A list of your following username
        """
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href, "
                                          "'/following')]").click()
        following = self._get_names()
        return following

    def _followers_section(self):
        """Returns all your followers

        Returns:
            A list of your followers username
        """
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href,"
                                          " '/followers')]").click()
        followers = self._get_names()
        return followers

    def _get_names(self):
        """Get all page id from following and followers box

        Returns:
            A list of username in the following or follower scroll box
        """
        time.sleep(random.randint(3, 5))
        scroll_box = self.driver.find_element_by_xpath("//div"
                                                       "[@class='_aano']")
        time.sleep(random.randint(5, 7))
        self._scroll_down(scroll_box)
        time.sleep(random.randint(3, 5))
        # received Page' id in following or followers box
        names = self._separate_names(scroll_box)
        time.sleep(2)
        # close scrol box
        pyautogui.press('esc')
        return names

    def _scroll_down(self, scroll_box):
        """Scrol down in following or followers box

        Args:
            scroll_box: Xpath element of scroll box instagram
        """
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(random.randint(2, 3))
            ht = self.driver.execute_script(""" 
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight; """, scroll_box)

    @staticmethod
    def _separate_names(scroll_box):
        """This part seperate username

        Args:
            scroll_box: Xpath element of scroll box instagram

        Returns:
            A list of usernames
            """
        links = scroll_box.find_elements_by_tag_name("a")
        time.sleep(random.randint(2, 3))
        # seperate names
        names = [name.text for name in links if name.text != '']
        return names

    def quit(self):
        self.driver.quit()
