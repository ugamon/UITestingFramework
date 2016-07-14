from config import BaseConfigEnterpreter
import UISelenium
from common.exceptions import WrongConfigKeyException



class Executor:
    def __call__(self, segment):
        step = BaseConfigEnterpreter().optionsAndKeysInSegment(segment)
        for key, value in step.items():
            print(key,value)
            try:
                getattr(UISelenium.StepsClass('https://moskva.beeline.ru'), key)(value)
            except AttributeError:
                raise WrongConfigKeyException

if __name__  == '__main__':
    ExecutorInst = Executor()
    segments = BaseConfigEnterpreter().SEGMENTS
    for i in segments:
        ExecutorInst(i)






