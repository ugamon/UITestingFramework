from config import BaseConfigEnterpreter
from UISelenium import StepsClass
from datetime import datetime,date

class OptionsMapper:

    def __init__(self):
        self.__BaseConfigEnterpreterInst = BaseConfigEnterpreter()


    def segmentsToActivate(self, list_of_options):
        return True if list_of_options[0][u'start'] == u'True' else False

    def commandsToExecute(self,segment):
        _ = self.__BaseConfigEnterpreterInst.optionsAndKeysInSegment(segment)
        if self.segmentsToActivate(_):
            return [self.executeEnterpreter(v) for v in _]

    def executeEnterpreter(self, step):
        print(step,segments)
        for key, value in step.items():

            if u'start' in key:
                 self.__StepsClassInst = StepsClass()
                 self.__StepsClassInst.start(self.__BaseConfigEnterpreterInst.URL)
            elif u'clickon' in key:
                if u'id' in value:
                    __ = value[value.find('(')+1:value.find(')')]
                    self.__StepsClassInst.click_on_focused_element(self.__StepsClassInst.get_element_by_id(value[value.find('(')+1:value.find(')')]))

                elif u'xpath' in value:
                    self.__StepsClassInst.click_on_focused_element(self.__StepsClassInst.get_element_by_xpath(value[value.find('(')+1:value.find(')')]))

                elif u'name' in value:
                    self.__StepsClassInst.click_on_focused_element(self.__StepsClassInst.get_element_by_name(value[value.find('(')+1:value.find(')')]))
            elif u'sendkeys' in key:

                self.__StepsClassInst.send_keys(value)

            elif u'printscreen' in key:

                self.__StepsClassInst.printscreen('{0}.png'.format(segments))

            elif u'shutdown' in key:
                self.__StepsClassInst.shutdown()

if __name__  == '__main__':
    OptionsMapperInst = OptionsMapper()
    segments = BaseConfigEnterpreter().SEGMENTS
    print([OptionsMapperInst.commandsToExecute(segments) for segments in segments if 'global' not in segments])






