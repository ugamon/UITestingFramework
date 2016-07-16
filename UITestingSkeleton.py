#encoding=utf-8

from config import BaseConfigEnterpreter
from common.exceptions import WrongConfigKeyException
from UISelenium import DRIVER
from common.helper import *
import UISelenium

LIST = {
    'segment1':
        [
            {'get_element_by_id': "lst-ib"},
            {'click_on_focused_element': 'true'},
            {'send_keys': 'привет$23434$'},
            {"shutdown": 'False'},
        ],
}


def executor(segment):

    #todo:сложно читаемый код, нужно переписать на что-то покороче

    DRIVER.get('http://google.com')
    for step in LIST[segment]:
        for key, value in step.items():
            try:
                UISelenium.strategy(getattr(UISelenium, key), convert_to_unicode(value))
            except AttributeError:
                print('Attribute error')




