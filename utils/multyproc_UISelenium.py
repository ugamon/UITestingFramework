from multiprocessing import Process,Pool,Lock
from UITestingSkeleton import OptionsMapper
from config import BaseConfigEnterpreter
from UISelenium import StepsClass
import os
from time import sleep

def fffff(x):
    return x*x

def func():
    return OptionsMapper()(BaseConfigEnterpreter.SEGMENTS[1], StepsClass())



