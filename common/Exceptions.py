# encoding=utf-8


class FileNotFoundException(Exception):
  def __init__(self):
      pass
  def __str__(self):
        exception_msg = "Message: %s\n" % 'Нет конфигурационного файла'
