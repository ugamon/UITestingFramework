# encoding=utf-8

from selenium import webdriver
from config import BaseConfigEnterpreter
from common.exceptions import WrongConfigKeyException
from testcase_step_handler import TestCaseHandler
from common.helper import *
import step_logic_over_selenium
import os

LIST = {
    'segment1':
        [
            {'get_element_by_id': "text"},
            {'click_on_focused_element': 'true'},
            {'send_keys': 'привет‚$23434$'},
            {"shutdown": 'False'},
        ],
}

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def executor(segment):

    #todo:СЃР»РѕР¶РЅРѕ С‡РёС‚Р°РµРјС‹Р№ РєРѕРґ, РЅСѓР¶РЅРѕ РїРµСЂРµРїРёСЃР°С‚СЊ РЅР° С‡С‚Рѕ-С‚Рѕ РїРѕРєРѕСЂРѕС‡Рµ

    #переопределение свойств управляющего класса
    handlerInst = TestCaseHandler()
    handlerInst.driver = webdriver.Chrome(os.path.join(CUR_DIR,'chromedriver.exe'))
    handlerInst.url = 'https://yandex.ru'
    #инициализация сессии Selenium и передача объекта в модуль step_logic_over_selenium
    handlerInst.driver.get(handlerInst.url)
    step_logic_over_selenium.DRIVER = handlerInst.driver

    for step in LIST[segment]:
        for key, value in step.items():
            try:
                handlerInst.strategy(getattr(step_logic_over_selenium, key), convert_to_unicode(value))
            except AttributeError:
                print('Attribute error')



executor('segment1')
