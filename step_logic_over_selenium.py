    # encoding=utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common import action_chains
from common.helper import convert_to_bool, select_from_list_if_true, singleton
import sys


def get_element_by_id(id, wait=10):
        """
        id
        """
        try:

            return WebDriverWait(DRIVER, wait).until(
                EC.presence_of_element_located((By.ID, id))
            )
        finally:
           pass

def get_element_by_xpath(xpath, wait=10):
        """
        xpath
        """
        try:
            return WebDriverWait(DRIVER, wait).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )

        finally:
            pass

def get_element_by_name(name, wait=10):
        """
        name
        """
        try:
            return WebDriverWait(DRIVER, wait).until(
                EC.presence_of_element_located((By.NAME, name))
            )

        finally:
            pass

def get_elements_by_xpath(xpath='//meta', wait=4):
        """
        xpath
        """
        try:
           return WebDriverWait(DRIVER, wait).until(
                     EC.presence_of_all_elements_located((By.XPATH, xpath)))

        finally:
            pass

def get_element_html_content(element):

    return element.get_attribute('innerHtml')

def focus_on_element(element):

        return action_chains.ActionChains(DRIVER).move_to_element(element).perform()

def click_on_focused_element(element):

        return action_chains.ActionChains(DRIVER).click(element).perform()

def send_keys(keys):

        return DRIVER.execute(Command.SEND_KEYS_TO_ACTIVE_ELEMENT, {'value': action_chains.ActionChains(DRIVER)._keys_to_typing(keys)})

def shutdown(key=False):

        if isinstance(key, bool) and key:
            return DRIVER.quit()
        else:
            try:
                if convert_to_bool(key):
                    return DRIVER.quit()
                else:
                    return DRIVER
            except TypeError:
                pass


