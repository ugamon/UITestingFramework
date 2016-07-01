# encoding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.selenium import selenium
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common import action_chains


CUR_DIR = os.path.dirname(os.path.abspath(__file__))


class StepsClass:

    def __init__(self):
        self.driver = webdriver.Chrome('{}//chromedriver.exe'.format(CUR_DIR))

    def __enter__(self):
        return self

    def start(self,url):
        self.driver.get(url)

    def get_element_by_id(self, id, wait=10):
        try:
            return WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((By.ID, id))
            )
        finally:
           pass

    def get_element_by_xpath(self, xpath, wait=10):
        try:
            return WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        finally:
            pass

    def get_element_by_name(self, name, wait=10):
        try:
            return WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located((By.NAME, name))
            )
        finally:
            pass

    def get_elements_by_xpath(self, xpath='//meta', wait=4):
        try:
           return WebDriverWait(self.driver, wait).until(
                     EC.presence_of_all_elements_located((By.XPATH, xpath)))

        finally:
            pass

    def printscreen(self, filename='printscreen.png'):
        return self.driver.get_screenshot_as_file(filename)


    # def focus_on_element(self, element):
    #     self.element = element
    #     return action_chains.ActionChains(self.driver).move_to_element(element).perform()

    def click_on_focused_element(self, element):
        self.element = element
        return action_chains.ActionChains(self.driver).click(element).perform()

    def send_keys(self, keys):
        return self.driver.execute(Command.SEND_KEYS_TO_ACTIVE_ELEMENT, {'value': action_chains.ActionChains(self.driver)._keys_to_typing(keys)})

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()

if __name__ == '__main__':

    with StepsClass() as inst:
        start = inst.start('https://www.python.org/')
        element1 = inst.get_element_by_id('id-search-field')
        inst.click_on_focused_element(element1)
        inst.send_keys(u'hello')
        inst.printscreen()



# {
#     "start":(url)
#     "step1":(click,),
#     "step2":(get_element_by_id('id'),),
#     "step3":(click(get_element_by_id)
#
#
# }