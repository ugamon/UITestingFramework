# encoding=utf-8

class TestCaseHandler(object):
    '''Класс управляющий шагами в тест кейсах.
    1)Свойства - объект Selenium.webdriver; Url - строка с урлом
    2)Метод strategy - стратегия исполнения
    '''

    def __init__(self):
        self._driver = None
        self._url = None
        self.element = list()

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self,value):
        self._driver = value

    @driver.deleter
    def driver(self):
        del self._driver

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @url.deleter
    def url(self):
        del self._url

    def strategy(self, stepobject, *args):

        #1) управляющая функция, в качестве аргументов передаются имя функции для исполнения и ее аргументы.
        #2) единственное место для управления глобальным списком element

        res = lambda: True if stepobject.__doc__ in ['id', 'xpath', 'name'] else False
        if res():
            self.element.append(stepobject(args[0]))
            return stepobject(args[0])
        else:
            stepobject(self.element.pop()) if len(self.element) else stepobject(args[0])

