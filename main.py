from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from print import print_, print_find
import time
import random
import pyautogui
import os


class Insta:

    def __init__(self, username, password, desired_page):
        self.username = username
        self.password = password
        self.id_taraf = desired_page
        self.driver = webdriver.Chrome()

    def login(self):
        # Desired page
        self.driver.get("https://www.instagram.com/{}/".format(self.id_taraf))
        time.sleep(random.randint(2, 5))

        # agar error dar vorod etelat shdo in ra comment kon
        # bayad ye if barash dorost konam khodesh tashkhis  bede
        # self.driver.find_element_by_xpath("//button[@type='button']").click()
        user_name = self.driver.find_element_by_xpath("//input"
                                                      "[@name='username']")
        user_name.send_keys(self.username)
        time.sleep(random.randint(2, 5))
        pass_word = self.driver.find_element_by_xpath("//input"
                                                      "[@name='password']")
        pass_word.send_keys(self.password + Keys.ENTER)
        # Ask for sms verification
        time.sleep(random.randint(5, 6))
        if ask == "y":
            self._verification_code()
        self._save_pass()

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
        # bakhshe peyda kardan
        not_following_back = [user_id for user_id in following if user_id \
                              not in followers]
        return not_following_back

    def _following_section(self):
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href, "
                                          "'/following')]").click()
        following = self._get_names()
        return following

    def _followers_section(self):
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
        # Close scrol box
        time.sleep(2)
        pyautogui.press('esc')
        return names

    def _scroll_down(self, scroll_box):
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(random.randint(2, 3))
            ht = self.driver.execute_script(""" 
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight; """, scroll_box)

    def _separate_names(self, scroll_box):
        # This part shows those who unfollowed your page
        links = scroll_box.find_elements_by_tag_name("a")
        time.sleep(random.randint(2, 3))
        names = [name.text for name in links if name.text != '']
        return names

    def quit(self):
        self.driver.quit()


class Generate:
    """Class to create a text file and show text file"""

    def __init__(self, page_id, unfollowed):
        self.page_id = page_id
        self.unfollowed = unfollowed
        self.file_name = f"{self.page_id}-file.txt"

    def write_txt(self):
        with open(self.file_name, "w") as f:
            f.write(f"These people did not follow this page({self.page_id}):")
            for num, name in enumerate(self.unfollowed):
                f.write(f"\n{num}- {name}")

    def show_txt(self):
        os.startfile(self.file_name)


if __name__ == "__main__":
    print_()
    user = input("pleas enter your username= ")
    pass_ = input("pleas enter your password= ")
    desired = input("-The desired page for find those= ")
    ask = input("-Did you enable verification Code?[y/n] ")

    insta = Insta(username=user, password=pass_, desired_page=desired)
    insta.login()
    find_unfollowed = insta.find()

    print_find(find_unfollowed, insta.id_taraf)

    txt = Generate(page_id=insta.id_taraf, unfollowed=find_unfollowed)
    txt.write_txt()
    txt.show_txt()

