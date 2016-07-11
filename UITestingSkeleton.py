from config import BaseConfigEnterpreter
from UISelenium import StepsClass
from datetime import datetime,date

class OptionsMapper:

    def __init__(self):
        self.__BaseConfigEnterpreterInst = BaseConfigEnterpreter()
        self.StepClassInst = StepsClass()

    def segmentsToActivate(self, list_of_options):
        return True if list_of_options[0][u'start'] == u'True' else False

    def __call__(self,segment):

        #self.segment = segment
        #_ = self.__BaseConfigEnterpreterInst.optionsAndKeysInSegment(segment)

        if self.segmentsToActivate(_):
             __ = self.__BaseConfigEnterpreterInst.optionsAndKeysInSegment(segment)
            return [self.executeEnterpreter(v,self.StepClassInst) for v in _]

    def executeEnterpreter(self, step, stepClassInst):
        print(step, stepClassInst)
        for key, value in step.items():

            if u'start' in key:
                 self.StepClassInst.start(self.__BaseConfigEnterpreterInst.URL)

            elif u'clickon' in key:

                if u'id' in value:
                    __ = value[value.find('(')+1:value.find(')')]
                    self.StepClassInst.click_on_focused_element(self.StepClassInst.get_element_by_id(value[value.find('(')+1:value.find(')')]))

                elif u'xpath' in value:
                    self.StepClassInst.click_on_focused_element(self.StepClassInst.get_element_by_xpath(value[value.find('(')+1:value.find(')')]))

                elif u'name' in value:
                    self.StepClassInst.click_on_focused_element(self.StepClassInst.get_element_by_name(value[value.find('(')+1:value.find(')')]))

            elif u'sendkeys' in key:

                stepClassInst.send_keys(value)

            elif u'printscreen' in key:

                stepClassInst.printscreen('{0}.png'.format(stepClassInst))

            elif u'shutdown' in key:
                stepClassInst.shutdown()

#if __name__  == '__main__':
#    OptionsMapperInst = OptionsMapper()
#    segments = BaseConfigEnterpreter().SEGMENTS
#    print([OptionsMapperInst(segments) for segments in segments if 'global' not in segments])






