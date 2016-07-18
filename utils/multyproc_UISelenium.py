from multiprocessing import Process,Pool,Lock
from core import OptionsMapper
from config import BaseConfigEnterpreter
from step_logic_over_selenium import StepsClass
import os
from time import sleep

def fffff(x):
    return x*x

def func():
    return OptionsMapper()(BaseConfigEnterpreter.SEGMENTS[1], StepsClass())



