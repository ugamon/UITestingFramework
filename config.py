# encoding=utf-8
import configparser

class BaseConfigEnterpreter:

   def __init__(self, config_file='configfile.txt'):
        self.__config = configparser.ConfigParser()
        self.__config.read('configfile.txt')
        self.SEGMENTS = self.__config.sections()
        self.URL = self.__config.get('global','url')

   def optionsAndKeysInSegment(self,segment):
       options_values_dict = self.__config.options(segment)
       return [{option: self.__config.get(segment, option)} for option in options_values_dict]


inst = BaseConfigEnterpreter()
