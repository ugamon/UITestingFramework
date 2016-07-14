    # encoding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common import action_chains
import datetime
import errno
from common.helper import convert_to_bool, select_from_list_if_true


CUR_DIR = os.path.dirname(os.path.abspath(__file__))


class StepsClass:

    def __init__(self,url):

        self.driver = webdriver.Chrome('{}//chromedriver.exe'.format(CUR_DIR))
        self.driver.get(url)



    def get_element_by_id(self, id, wait=10):
        try:

            return True, WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((By.ID, id))
            )
        finally:
           pass

    def get_element_by_xpath(self, xpath, wait=10):
        try:
            return True, WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )

        finally:
            pass

    def get_element_by_name(self, name, wait=10):
        try:
            return True, WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((By.NAME, name))
            )

        finally:
            pass

    def get_elements_by_xpath(self, xpath='//meta', wait=4):
        try:
           return True, WebDriverWait(self.driver, wait).until(
                     EC.presence_of_all_elements_located((By.XPATH, xpath)))

        finally:
            pass

    def printscreen(self, filename='printscreen.png'):
        try:
            desired_path = os.path.join(CUR_DIR, 'screenshots', datetime.date.today().__str__())
            if os.path.exists(desired_path):
                filepath = os.path.join(desired_path, filename)
            else:
                os.makedirs(desired_path)
                filepath = os.path.join(desired_path, filename)
            return self.driver.get_screenshot_as_file(filepath)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise



    def focus_on_element(self, element):
        return action_chains.ActionChains(self.driver).move_to_element(element).perform()

    def click_on_focused_element(self, element):

        return action_chains.ActionChains(self.driver).click(element).perform()

    def send_keys(self, keys):
        return self.driver.execute(Command.SEND_KEYS_TO_ACTIVE_ELEMENT, {'value': action_chains.ActionChains(self.driver)._keys_to_typing(keys)})

    def shutdown(self, key=False):

        if isinstance(key, bool) and key:
            return self.driver.quit()
        else:
            try:
                if convert_to_bool(key):
                    return self.driver.quit()
                else:
                    return self.driver
            except TypeError:
                pass

    def __exit__(self):
        pass


print(StepsClass('https://beedate.beeline.ru/').get_element_by_name('ctn')[1])

# {
#     "start":(url)
#     "step1":(click,),
#     "step2":(get_element_by_id('id'),),
#     "step3":(click(get_element_by_id)
#
#
# }