# encoding=utf-8

from selenium import webdriver

from common.exceptions import WrongConfigKeyException
from testcase_step_handler import TestCaseHandler
from common.helper import *
import step_logic_over_selenium
import os

LIST = {
    'tc 1':
        [
            {'get_element_by_id': "DV_Header"},
            {'click_on_focused_element': 'true'},

            {'get_element_by_xpath': '//a[@href="/customers/do-you-know-beeline/"]'},
            {'click_on_focused_element': 'true'},

            {'get_element_by_xpath': '//button[contains(.,"Получать бонусы")]'},
            {'click_on_focused_element': 'true'},


            {'get_element_by_id': "login"},
            {'click_on_focused_element': 'true'},
            {'send_keys': '9652996612'},
            {'get_element_by_name': "password"},
            {'click_on_focused_element': 'true'},
            {'send_keys': 'Citibank09'},

            {'printscreen': 'fifth'},

            {'get_element_by_id': "submitLabel"},
            {'click_on_focused_element': 'true'},

            {'get_element_by_xpath': '//a[contains(.,"Посмотреть все бонусы и скидки")]'},
            {'click_on_focused_element': 'true'},

            {'printscreen': 'six'},
            {'get_element_by_xpath': '//div[@class="_18Rer _2y_Vd"]'},
            {'get_element_html_content': 'true'}
        ],
}

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

def executor(segment):

    #todo:СЃР»РѕР¶РЅРѕ С‡РёС‚Р°РµРјС‹Р№ РєРѕРґ, РЅСѓР¶РЅРѕ РїРµСЂРµРїРёСЃР°С‚СЊ РЅР° С‡С‚Рѕ-С‚Рѕ РїРѕРєРѕСЂРѕС‡Рµ

    #переопределение свойств управляющего класса
    handlerInst = TestCaseHandler()
    handlerInst.driver = webdriver.Chrome(os.path.join(CUR_DIR,'chromedriver.exe'))
    handlerInst.url = 'https://moskva.beeline.ru'
    #инициализация сессии Selenium и передача объекта в модуль step_logic_over_selenium
    handlerInst.driver.get(handlerInst.url)
    step_logic_over_selenium.DRIVER = handlerInst.driver
    step_logic_over_selenium.CUR_DIR = CUR_DIR


    for step in LIST[segment]:
        for key, value in step.items():
            try:
                handlerInst.strategy(getattr(step_logic_over_selenium, key), convert_to_unicode(value))
            except AttributeError:
                print('Attribute error')



executor('tc 1')
