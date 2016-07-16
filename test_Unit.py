#encoding=utf-8
from unittest import TestCase
from selenium import webdriver
import os
import UISelenium
CUR_DIR = os.path.dirname(os.path.abspath(__file__))

class UiFrameWorkTest(TestCase):

    def setUp(self):
        self.DRIVER = webdriver.Chrome('{}//chromedriver.exe'.format(CUR_DIR))
        self.DRIVER.get('https://google.com')

    def test_strategy_id(self):
        pass


    def tearDown(self):
        self.DRIVER.quit()


