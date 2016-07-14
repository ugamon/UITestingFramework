# encoding=utf-8
import configparser as configparser
import os
from common import exceptions

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
config_file = 'configfile'


def readConfigFile(configFile='configfile.txt'):
     config_file_object    = configparser.ConfigParser()
     file_read_object =config_file_object.read(os.path.join(CUR_DIR, configFile))
     if len(file_read_object):
         return config_file_object
     else:
         raise exceptions.FileNotFoundException


class BaseConfigEnterpreter:

   SEGMENTS = readConfigFile().sections()

   def __init__(self, config_file='configfile.txt'):
        self.FILENAME = os.path.join(CUR_DIR,config_file)
        self.__config = configparser.ConfigParser()
        self.__config.read(self.FILENAME)
        self.SEGMENTS = self.__config.sections()
        #self.URL = self.__config.get('global','url')

   def optionsAndKeysInSegment(self, segment):
       a = dict()
       options = readConfigFile().options(segment)
       for option in options:
          a.update({option:readConfigFile().get(segment,option)})
       return a





